from __future__ import unicode_literals

from django.db import models


class RelationType(models.Model):
    text = models.CharField(max_length=60, blank=False)


class GenericObjectRelation(models.Model):
    first_model_id = models.IntegerField(blank=False, null=False)
    second_model_id = models.IntegerField(blank=False, null=False)
    relation_type = models.IntegerField(blank=False, null=False)


class RelationManager(object):

    @staticmethod
    def add_relation(m1, m2, rt):
        rel = GenericObjectRelation()
        rel.first_model_id = m1
        rel.second_model_id = m2
        rel.relation_type = rt
        rel.save()

    @staticmethod
    def get_relations(m):
        relations = []
        for rel in GenericObjectRelation.objects.all():
            if rel.first_model_id == m or rel.second_model_id == m:
                relations.append(rel)
        return relations

    @staticmethod
    def delete_relation(_id):
        rel = GenericObjectRelation.objects.get(id=_id)
        rel.delete()
