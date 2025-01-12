/*
 * TencentBlueKing is pleased to support the open source community by making
 * 蓝鲸智云 - API 网关(BlueKing - APIGateway) available.
 * Copyright (C) 2017 THL A29 Limited, a Tencent company. All rights reserved.
 * Licensed under the MIT License (the "License"); you may not use this file except
 * in compliance with the License. You may obtain a copy of the License at
 *
 *     http://opensource.org/licenses/MIT
 *
 * Unless required by applicable law or agreed to in writing, software distributed under
 * the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
 * either express or implied. See the License for the specific language governing permissions and
 * limitations under the License.
 *
 * We undertake not to change the open source license (MIT license) applicable
 * to the current version of the project delivered to anyone in the future.
 */
/**
 * @file 引入 bk-magic-vue 组件
 * @author
 */

import Vue from 'vue'

// 全量引入
// import './fully-import'

// 按需引入
import './demand-import'

const Message = Vue.prototype.$bkMessage

let messageInstance = null

export const messageError = (message, delay = 3000) => {
  messageInstance && messageInstance.close()
  messageInstance = Message({
    message,
    delay,
    theme: 'error'
  })
}

export const messageSuccess = (message, delay = 3000) => {
  messageInstance && messageInstance.close()
  messageInstance = Message({
    message,
    delay,
    theme: 'success'
  })
}

export const messageInfo = (message, delay = 3000) => {
  messageInstance && messageInstance.close()
  messageInstance = Message({
    message,
    delay,
    theme: 'primary'
  })
}

export const messageWarn = (message, delay = 3000) => {
  messageInstance && messageInstance.close()
  messageInstance = Message({
    message,
    delay,
    theme: 'warning',
    hasCloseIcon: true
  })
}

Vue.prototype.messageError = messageError
Vue.prototype.messageSuccess = messageSuccess
Vue.prototype.messageInfo = messageInfo
Vue.prototype.messageWarn = messageWarn
