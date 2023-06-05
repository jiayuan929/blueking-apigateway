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
# Generated by Django 2.0.13 on 2022-03-07 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("schema", "0004_auto_20200528_1140"),
    ]

    operations = [
        migrations.AlterField(
            model_name="schema",
            name="type",
            field=models.CharField(
                choices=[
                    ("context", "CONTEXT"),
                    ("proxy", "PROXY"),
                    ("access_strategy", "ACCESS_STRATEGY"),
                    ("plugin", "PLUGIN"),
                    ("monitor", "MONITOR"),
                    ("apisdk", "APISDK"),
                    ("micro_gateway", "MICRO_GATEWAY"),
                    ("backend_service", "BACKEND_SERVICE"),
                ],
                max_length=32,
            ),
        ),
    ]