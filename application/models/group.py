#coding: utf-8
from whirlwind.db.mongo import Mongo
from pymongo.objectid import ObjectId
from pymongo import ASCENDING, DESCENDING
from mongokit import *
import datetime
from application.models.organization import Organization


@Mongo.db.connection.register
class Group(Document):
    '''
        profession - специальность (МО)
        created_at - дата образования группы
        graduated - выпустилась ли группа
    '''
    structure = {
        'organization': {
            'id': ObjectId,
            'name': unicode
        },
        'profession': unicode,
        'created_at': datetime.datetime,
        'name': unicode,
        'graduated': bool
    }

    required_fields = ['organization', 'profession', 'created_at', 'graduated']

    default_values = {'graduated': False}

    use_dot_notation = True

    @staticmethod
    def instance(name, profession, created_at, graduated, organization_id):
        group = Mongo.db.ui.groups.Group()
        group.name = name
        group.profession = profession
        group.created_at = created_at
        group.graduated = graduated
        group.organization.id = organization_id
        group.organization.name = Organization.get_by('_id', organization_id).name
        return group

    @staticmethod
    def create_group(name, profession, created_at, graduated, organization_id):
        group = Group.instance(name, profession, created_at, graduated, organization_id)
        Mongo.db.ui.groups.insert(group)

    @staticmethod
    def update_group(_id, name, profession, created_at, graduated, organization_id):
        Mongo.db.ui.groups.update(
            {'_id': _id},
            {'$set': {'name': name,
                      'profession': profession,
                      'created_at': created_at,
                      'graduated': graduated,
                      'organization.id': organization_id,
                      'Organization.name': Organization.get_by('_id', organization_id).name}}
        )

    @staticmethod
    def get_by(field, value):
        return Mongo.db.ui.groups.Group.find_one({field: value})

    @staticmethod
    def get_all(sorter='name', direction=1):
        return Mongo.db.ui.groups.Group.find().sort(sorter, ASCENDING if int(direction) == 1 else DESCENDING)

    @staticmethod
    def remove(_id):
        Mongo.db.ui.groups.remove({'_id': _id})

    @staticmethod
    def select_field_choises(organization_id=None):
        if organization_id is None:
            def select_item(group):
                return unicode(group._id), '{} ({} курс, {})'.format(group.name, group.get_course(), group.organization.name)
            choises = map(select_item, Mongo.db.ui.groups.Group.find().sort('name', ASCENDING))
        else:
            def select_item(group):
                return unicode(group._id), '{} ({} курс)'.format(group.name, group.get_course())
            choises = map(select_item, Mongo.db.ui.groups.Group.find({'organization.id': organization_id}).sort('name', ASCENDING))

        return choises

    def get_course(self):
        return (datetime.datetime.utcnow() - self.created_at).days / 365 + 1
