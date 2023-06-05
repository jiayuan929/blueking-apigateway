#
# TencentBlueKing is pleased to support the open source community by making
# 蓝鲸智云 - API 网关(BlueKing - APIGateway) available.
# Copyright (C) 2017 THL A29 Limited, a Tencent company. All rights reserved.
# Licensed under the MIT License (the "License"); you may not use this file except
# in compliance with the License. You may obtain a copy of the License at
#
#     http://opensource.org/licenses/MIT
#
# Unless required by applicable law or agreed to in writing, software distributed under
# the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
# either express or implied. See the License for the specific language governing permissions and
# limitations under the License.
#
# We undertake not to change the open source license (MIT license) applicable
# to the current version of the project delivered to anyone in the future.
#
# Generated by Django 2.0.13 on 2020-09-28 09:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0012_resource_allow_apply_permission"),
    ]

    operations = [
        migrations.CreateModel(
            name="ReleasedResource",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("created_time", models.DateTimeField(auto_now_add=True, null=True)),
                ("updated_time", models.DateTimeField(auto_now=True, null=True)),
                ("resource_version_id", models.IntegerField(db_index=True)),
                ("resource_id", models.IntegerField(db_index=True)),
                ("resource_name", models.CharField(blank=True, default="", max_length=256)),
                ("resource_method", models.CharField(max_length=10)),
                ("resource_path", models.CharField(max_length=2048)),
                ("_data", models.TextField(db_column="data", help_text="resource data in resource version")),
                ("api", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="core.API")),
            ],
            options={
                "verbose_name": "ReleasedResource",
                "verbose_name_plural": "ReleasedResource",
                "db_table": "core_released_resource",
            },
        ),
        migrations.AlterUniqueTogether(
            name="releasedresource",
            unique_together={("api", "resource_version_id", "resource_id")},
        ),
    ]