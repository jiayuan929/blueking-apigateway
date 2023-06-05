# -*- coding: utf-8 -*-
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
import pytest
from ddf import G
from django.core.management.base import CommandError

from apigateway.core.management.commands.update_jwt_key import Command
from apigateway.core.models import JWT, Gateway

pytestmark = pytest.mark.django_db


class TestCommand:
    @pytest.mark.parametrize(
        "api_name, private_key, public_key, expected_error",
        [
            (
                "test-update-jwt-key",
                "LS0tLS1CRUdJTiBSU0EgUFJJVkFURSBLRVktLS0tLQpNSUlFb2dJQkFBS0NBUUVBNmJLUlpmUmRobVdYUSt1Y2MyanVvQXN0WVVmMFRQUTRlcFRRZ3c3Qkd2a05tRXBUCjI2YlJ4UldqcDdGSWVZQzk3WEdTZ3Y4N0R0K1dhenBWeUhSNUlEU1FQZk9pOHV6WFZydTNQSjFrZ0xwa1NNVXkKV1F0eU55bTBxcDJBeWxlUlBBQ01Db0dTbnh2b2c3dmVodlhKc0YyejltREp1Nlp3UENjdXB5TTdhY0ZvaEU5WgpmWC9CZXRBNXNtZ1Y5ckVqVlNJbEtuNWZ1UjRCOHF5NThwVHdrMWVBY2h0NlNzNTdNbThRaDdaOGcwenEvWHJuCklCd2VmdDFydUdQb3BYR2JOSWhDQXVES0JLaWlUVjBZT1dwczBxdFllOXRtQzVqQ1BIM29mNzdRQW00YTlqbm4KR01XKyttUlN2VFZ4WHlSa0ZuKzVFL2NueWtLVHB2aGRpU1RaTlFJREFRQUJBb0lCQURzUnBJaWxwSUlVNlpBRQpYSzRiSnIyVE5hd3lHTURldGV2ZDgzbzgzM2htM1JYU0s3SUlUMXRHWmZBNzhqcXIzTlhJY0NUbVNGSXhGMzhRCjVwL2RPTVI0Sk1GVDlLcjhURTJpOHVUQ1Q2WHQ5dTBoMHVFSThKeWEwUXlTOVB1ditJaTNCcTZkSTZkTjBZNkMKalBPRjZxM0djWGRqN1htZHp4NlZOTWlRTWpNL2NQb2lubklwY1hpbFp1UXRYd1UvNWdmcVc4ZFdzRWhlR1RuZQptbHBXVjBURHBDWFBCNXBrV0pTMlYwZjdlenZlVHFEZHhNVVJtZGNVYkVNa0dUN1huVWkzZWVyU1ZsZ05zNS9oCnloU3VtRmg2Y1FvZmFuWU5jcXpxUDNqYjFYS1owLzVyczloRitTNk1nWjI5Wk9SQ1NQcDJVNGFsWDNpYUs0dnoKU0pJL1JMMENnWUVBODF6VGVna01PcW84WDVlRUkyYk01NEhHeTBsVnVjd1pTMk9VL1R6Mm5pamllQklQcWk1MQpqekxNS0N2eWJnRGFJRitSV0dmMDV5bW5ZLzg3YXc3MU5zUWFGeHgrWlNkbHFQMTV5c240NlBBWTdWdnh2Y3JxCjN1OG1IMjhYaEIzdU9LK1dkYk1XV2tnd3JPbml0K1RkZHVZV0ZnYlhlZ3dsMFVtcXJsQ0F6QWNDZ1lFQTlkVkMKQ0xTcVhUSHRDN1JOQ0pNblZQRVJ3emh6NXAzWEhTVVlNb1N0ODhtb0tDUm54bUlycUI5ZGZMYm5RaGNzQk1pMgo2Mks3VU5wUWkxNlhMdjBDLzBGRWdpNVoyR0VDTWMzSmxrOTFSU2V2emZJdEx2SGhHNGpieGp3NjFXblZzVGhnCi9FajlScDB3VXBITC8vaE56TTBGZ2tYdmFjWnVxaUZiNVBLUzJlTUNnWUJmVnk5MmNOTDhyTExJVkdpdElkb0cKbkg0UUtDUFFqVmdmZzl6YnRTVjg0dEdPYnF6NlpBY2tXYWRIMmFlNVZ0WWR0ck1QYW5LMG1VbjkwQUVzT1FqeQpNck54K0hUQUZrWXFoVnRRaWYzYzdDc24ya3lEcVZxSWlqSnFRREI3VHVxRUJLNHlZRDNTa3RPVyttNGEweXU4CkovbmhHVDhUam16R2FGRFl4NnNkd3dLQmdDeDQrQWs3SmRiV1FWdnNza0xxM0NLeHVkVG5VWkJXM2FPWUlsaUIKU0RiaU5GbU92SGRYS3k2dS9lcWg3QlE0dk8zZ29iYlRsYTk2enpkblZWSmEwei82UHJxT1NCS3MrZ2lvZ2Q5LwpZR2V5Vmt1YmxERDU4UTlhSXVncDNUcmVlcG9rNk9hN0RaYkl1UVUyK3dERG1zK0NCNDBadWNZWTc4dzNYTGgrCmFiS2hBb0dBQkdUTHdnSERJaDNmNWdSL3FTSEJaeXZVVUtDeGozbkpqckR1azdCYUtrTGhTdUdVY090Zm1uZEsKMnY5QWRUc2JRb1paeW9XaG44UFhIRGdqTmV1ZE5FR2h4Zm9Oc1lsbC9NYkdUVHEyMUx1RWFkTFMyMkE5SjBndQpTN245N2RBS2lzUEZ6TG5nSDFaaTBTbnV0L0p2M1J5WHZ6NGZtcHVlc3BudllKOUd6WU09Ci0tLS0tRU5EIFJTQSBQUklWQVRFIEtFWS0tLS0t",  # noqa
                "LS0tLS1CRUdJTiBQVUJMSUMgS0VZLS0tLS0KTUlJQklqQU5CZ2txaGtpRzl3MEJBUUVGQUFPQ0FROEFNSUlCQ2dLQ0FRRUE2YktSWmZSZGhtV1hRK3VjYzJqdQpvQXN0WVVmMFRQUTRlcFRRZ3c3Qkd2a05tRXBUMjZiUnhSV2pwN0ZJZVlDOTdYR1Nndjg3RHQrV2F6cFZ5SFI1CklEU1FQZk9pOHV6WFZydTNQSjFrZ0xwa1NNVXlXUXR5TnltMHFwMkF5bGVSUEFDTUNvR1NueHZvZzd2ZWh2WEoKc0YyejltREp1Nlp3UENjdXB5TTdhY0ZvaEU5WmZYL0JldEE1c21nVjlyRWpWU0lsS241ZnVSNEI4cXk1OHBUdwprMWVBY2h0NlNzNTdNbThRaDdaOGcwenEvWHJuSUJ3ZWZ0MXJ1R1BvcFhHYk5JaENBdURLQktpaVRWMFlPV3BzCjBxdFllOXRtQzVqQ1BIM29mNzdRQW00YTlqbm5HTVcrK21SU3ZUVnhYeVJrRm4rNUUvY255a0tUcHZoZGlTVFoKTlFJREFRQUIKLS0tLS1FTkQgUFVCTElDIEtFWS0tLS0t",  # noqa
                None,
            ),
            (
                "test-update-jwt-key",
                "not-base64-string",
                "not-base64-string",
                CommandError,
            ),
            # jwt key not match
            (
                "not-exist-gateway",
                "LS0tLS1CRUdJTiBSU0EgUFJJVkFURSBLRVktLS0tLQpNSUlFb2dJQkFBS0NBUUVBNmJLUlpmUmRobVdYUSt1Y2MyanVvQXN0WVVmMFRQUTRlcFRRZ3c3Qkd2a05tRXBUCjI2YlJ4UldqcDdGSWVZQzk3WEdTZ3Y4N0R0K1dhenBWeUhSNUlEU1FQZk9pOHV6WFZydTNQSjFrZ0xwa1NNVXkKV1F0eU55bTBxcDJBeWxlUlBBQ01Db0dTbnh2b2c3dmVodlhKc0YyejltREp1Nlp3UENjdXB5TTdhY0ZvaEU5WgpmWC9CZXRBNXNtZ1Y5ckVqVlNJbEtuNWZ1UjRCOHF5NThwVHdrMWVBY2h0NlNzNTdNbThRaDdaOGcwenEvWHJuCklCd2VmdDFydUdQb3BYR2JOSWhDQXVES0JLaWlUVjBZT1dwczBxdFllOXRtQzVqQ1BIM29mNzdRQW00YTlqbm4KR01XKyttUlN2VFZ4WHlSa0ZuKzVFL2NueWtLVHB2aGRpU1RaTlFJREFRQUJBb0lCQURzUnBJaWxwSUlVNlpBRQpYSzRiSnIyVE5hd3lHTURldGV2ZDgzbzgzM2htM1JYU0s3SUlUMXRHWmZBNzhqcXIzTlhJY0NUbVNGSXhGMzhRCjVwL2RPTVI0Sk1GVDlLcjhURTJpOHVUQ1Q2WHQ5dTBoMHVFSThKeWEwUXlTOVB1ditJaTNCcTZkSTZkTjBZNkMKalBPRjZxM0djWGRqN1htZHp4NlZOTWlRTWpNL2NQb2lubklwY1hpbFp1UXRYd1UvNWdmcVc4ZFdzRWhlR1RuZQptbHBXVjBURHBDWFBCNXBrV0pTMlYwZjdlenZlVHFEZHhNVVJtZGNVYkVNa0dUN1huVWkzZWVyU1ZsZ05zNS9oCnloU3VtRmg2Y1FvZmFuWU5jcXpxUDNqYjFYS1owLzVyczloRitTNk1nWjI5Wk9SQ1NQcDJVNGFsWDNpYUs0dnoKU0pJL1JMMENnWUVBODF6VGVna01PcW84WDVlRUkyYk01NEhHeTBsVnVjd1pTMk9VL1R6Mm5pamllQklQcWk1MQpqekxNS0N2eWJnRGFJRitSV0dmMDV5bW5ZLzg3YXc3MU5zUWFGeHgrWlNkbHFQMTV5c240NlBBWTdWdnh2Y3JxCjN1OG1IMjhYaEIzdU9LK1dkYk1XV2tnd3JPbml0K1RkZHVZV0ZnYlhlZ3dsMFVtcXJsQ0F6QWNDZ1lFQTlkVkMKQ0xTcVhUSHRDN1JOQ0pNblZQRVJ3emh6NXAzWEhTVVlNb1N0ODhtb0tDUm54bUlycUI5ZGZMYm5RaGNzQk1pMgo2Mks3VU5wUWkxNlhMdjBDLzBGRWdpNVoyR0VDTWMzSmxrOTFSU2V2emZJdEx2SGhHNGpieGp3NjFXblZzVGhnCi9FajlScDB3VXBITC8vaE56TTBGZ2tYdmFjWnVxaUZiNVBLUzJlTUNnWUJmVnk5MmNOTDhyTExJVkdpdElkb0cKbkg0UUtDUFFqVmdmZzl6YnRTVjg0dEdPYnF6NlpBY2tXYWRIMmFlNVZ0WWR0ck1QYW5LMG1VbjkwQUVzT1FqeQpNck54K0hUQUZrWXFoVnRRaWYzYzdDc24ya3lEcVZxSWlqSnFRREI3VHVxRUJLNHlZRDNTa3RPVyttNGEweXU4CkovbmhHVDhUam16R2FGRFl4NnNkd3dLQmdDeDQrQWs3SmRiV1FWdnNza0xxM0NLeHVkVG5VWkJXM2FPWUlsaUIKU0RiaU5GbU92SGRYS3k2dS9lcWg3QlE0dk8zZ29iYlRsYTk2enpkblZWSmEwei82UHJxT1NCS3MrZ2lvZ2Q5LwpZR2V5Vmt1YmxERDU4UTlhSXVncDNUcmVlcG9rNk9hN0RaYkl1UVUyK3dERG1zK0NCNDBadWNZWTc4dzNYTGgrCmFiS2hBb0dBQkdUTHdnSERJaDNmNWdSL3FTSEJaeXZVVUtDeGozbkpqckR1azdCYUtrTGhTdUdVY090Zm1uZEsKMnY5QWRUc2JRb1paeW9XaG44UFhIRGdqTmV1ZE5FR2h4Zm9Oc1lsbC9NYkdUVHEyMUx1RWFkTFMyMkE5SjBndQpTN245N2RBS2lzUEZ6TG5nSDFaaTBTbnV0L0p2M1J5WHZ6NGZtcHVlc3BudllKOUd6WU09Ci0tLS0tRU5EIFJTQSBQUklWQVRFIEtFWS0tLS0t",  # noqa
                "dGVzdA==",
                CommandError,
            ),
            # api not found
            (
                "not-exist-gateway",
                "LS0tLS1CRUdJTiBSU0EgUFJJVkFURSBLRVktLS0tLQpNSUlFb2dJQkFBS0NBUUVBNmJLUlpmUmRobVdYUSt1Y2MyanVvQXN0WVVmMFRQUTRlcFRRZ3c3Qkd2a05tRXBUCjI2YlJ4UldqcDdGSWVZQzk3WEdTZ3Y4N0R0K1dhenBWeUhSNUlEU1FQZk9pOHV6WFZydTNQSjFrZ0xwa1NNVXkKV1F0eU55bTBxcDJBeWxlUlBBQ01Db0dTbnh2b2c3dmVodlhKc0YyejltREp1Nlp3UENjdXB5TTdhY0ZvaEU5WgpmWC9CZXRBNXNtZ1Y5ckVqVlNJbEtuNWZ1UjRCOHF5NThwVHdrMWVBY2h0NlNzNTdNbThRaDdaOGcwenEvWHJuCklCd2VmdDFydUdQb3BYR2JOSWhDQXVES0JLaWlUVjBZT1dwczBxdFllOXRtQzVqQ1BIM29mNzdRQW00YTlqbm4KR01XKyttUlN2VFZ4WHlSa0ZuKzVFL2NueWtLVHB2aGRpU1RaTlFJREFRQUJBb0lCQURzUnBJaWxwSUlVNlpBRQpYSzRiSnIyVE5hd3lHTURldGV2ZDgzbzgzM2htM1JYU0s3SUlUMXRHWmZBNzhqcXIzTlhJY0NUbVNGSXhGMzhRCjVwL2RPTVI0Sk1GVDlLcjhURTJpOHVUQ1Q2WHQ5dTBoMHVFSThKeWEwUXlTOVB1ditJaTNCcTZkSTZkTjBZNkMKalBPRjZxM0djWGRqN1htZHp4NlZOTWlRTWpNL2NQb2lubklwY1hpbFp1UXRYd1UvNWdmcVc4ZFdzRWhlR1RuZQptbHBXVjBURHBDWFBCNXBrV0pTMlYwZjdlenZlVHFEZHhNVVJtZGNVYkVNa0dUN1huVWkzZWVyU1ZsZ05zNS9oCnloU3VtRmg2Y1FvZmFuWU5jcXpxUDNqYjFYS1owLzVyczloRitTNk1nWjI5Wk9SQ1NQcDJVNGFsWDNpYUs0dnoKU0pJL1JMMENnWUVBODF6VGVna01PcW84WDVlRUkyYk01NEhHeTBsVnVjd1pTMk9VL1R6Mm5pamllQklQcWk1MQpqekxNS0N2eWJnRGFJRitSV0dmMDV5bW5ZLzg3YXc3MU5zUWFGeHgrWlNkbHFQMTV5c240NlBBWTdWdnh2Y3JxCjN1OG1IMjhYaEIzdU9LK1dkYk1XV2tnd3JPbml0K1RkZHVZV0ZnYlhlZ3dsMFVtcXJsQ0F6QWNDZ1lFQTlkVkMKQ0xTcVhUSHRDN1JOQ0pNblZQRVJ3emh6NXAzWEhTVVlNb1N0ODhtb0tDUm54bUlycUI5ZGZMYm5RaGNzQk1pMgo2Mks3VU5wUWkxNlhMdjBDLzBGRWdpNVoyR0VDTWMzSmxrOTFSU2V2emZJdEx2SGhHNGpieGp3NjFXblZzVGhnCi9FajlScDB3VXBITC8vaE56TTBGZ2tYdmFjWnVxaUZiNVBLUzJlTUNnWUJmVnk5MmNOTDhyTExJVkdpdElkb0cKbkg0UUtDUFFqVmdmZzl6YnRTVjg0dEdPYnF6NlpBY2tXYWRIMmFlNVZ0WWR0ck1QYW5LMG1VbjkwQUVzT1FqeQpNck54K0hUQUZrWXFoVnRRaWYzYzdDc24ya3lEcVZxSWlqSnFRREI3VHVxRUJLNHlZRDNTa3RPVyttNGEweXU4CkovbmhHVDhUam16R2FGRFl4NnNkd3dLQmdDeDQrQWs3SmRiV1FWdnNza0xxM0NLeHVkVG5VWkJXM2FPWUlsaUIKU0RiaU5GbU92SGRYS3k2dS9lcWg3QlE0dk8zZ29iYlRsYTk2enpkblZWSmEwei82UHJxT1NCS3MrZ2lvZ2Q5LwpZR2V5Vmt1YmxERDU4UTlhSXVncDNUcmVlcG9rNk9hN0RaYkl1UVUyK3dERG1zK0NCNDBadWNZWTc4dzNYTGgrCmFiS2hBb0dBQkdUTHdnSERJaDNmNWdSL3FTSEJaeXZVVUtDeGozbkpqckR1azdCYUtrTGhTdUdVY090Zm1uZEsKMnY5QWRUc2JRb1paeW9XaG44UFhIRGdqTmV1ZE5FR2h4Zm9Oc1lsbC9NYkdUVHEyMUx1RWFkTFMyMkE5SjBndQpTN245N2RBS2lzUEZ6TG5nSDFaaTBTbnV0L0p2M1J5WHZ6NGZtcHVlc3BudllKOUd6WU09Ci0tLS0tRU5EIFJTQSBQUklWQVRFIEtFWS0tLS0t",  # noqa
                "LS0tLS1CRUdJTiBQVUJMSUMgS0VZLS0tLS0KTUlJQklqQU5CZ2txaGtpRzl3MEJBUUVGQUFPQ0FROEFNSUlCQ2dLQ0FRRUE2YktSWmZSZGhtV1hRK3VjYzJqdQpvQXN0WVVmMFRQUTRlcFRRZ3c3Qkd2a05tRXBUMjZiUnhSV2pwN0ZJZVlDOTdYR1Nndjg3RHQrV2F6cFZ5SFI1CklEU1FQZk9pOHV6WFZydTNQSjFrZ0xwa1NNVXlXUXR5TnltMHFwMkF5bGVSUEFDTUNvR1NueHZvZzd2ZWh2WEoKc0YyejltREp1Nlp3UENjdXB5TTdhY0ZvaEU5WmZYL0JldEE1c21nVjlyRWpWU0lsS241ZnVSNEI4cXk1OHBUdwprMWVBY2h0NlNzNTdNbThRaDdaOGcwenEvWHJuSUJ3ZWZ0MXJ1R1BvcFhHYk5JaENBdURLQktpaVRWMFlPV3BzCjBxdFllOXRtQzVqQ1BIM29mNzdRQW00YTlqbm5HTVcrK21SU3ZUVnhYeVJrRm4rNUUvY255a0tUcHZoZGlTVFoKTlFJREFRQUIKLS0tLS1FTkQgUFVCTElDIEtFWS0tLS0t",  # noqa
                CommandError,
            ),
        ],
    )
    def test_handle(self, api_name, private_key, public_key, expected_error):
        gateway = G(Gateway, name="test-update-jwt-key")
        jwt = G(JWT, api=gateway)

        if expected_error is None:
            Command().handle(api_name, private_key, public_key)
            return

        with pytest.raises(expected_error):
            Command().handle(api_name, private_key, public_key)