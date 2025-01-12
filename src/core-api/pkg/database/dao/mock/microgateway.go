// Code generated by MockGen. DO NOT EDIT.
// Source: microgateway.go

// Package mock is a generated GoMock package.
package mock

import (
	dao "core/pkg/database/dao"
	reflect "reflect"

	gomock "github.com/golang/mock/gomock"
)

// MockMicroGatewayManager is a mock of MicroGatewayManager interface.
type MockMicroGatewayManager struct {
	ctrl     *gomock.Controller
	recorder *MockMicroGatewayManagerMockRecorder
}

// MockMicroGatewayManagerMockRecorder is the mock recorder for MockMicroGatewayManager.
type MockMicroGatewayManagerMockRecorder struct {
	mock *MockMicroGatewayManager
}

// NewMockMicroGatewayManager creates a new mock instance.
func NewMockMicroGatewayManager(ctrl *gomock.Controller) *MockMicroGatewayManager {
	mock := &MockMicroGatewayManager{ctrl: ctrl}
	mock.recorder = &MockMicroGatewayManagerMockRecorder{mock}
	return mock
}

// EXPECT returns an object that allows the caller to indicate expected use.
func (m *MockMicroGatewayManager) EXPECT() *MockMicroGatewayManagerMockRecorder {
	return m.recorder
}

// Get mocks base method.
func (m *MockMicroGatewayManager) Get(instanceID string) (dao.MicroGateway, error) {
	m.ctrl.T.Helper()
	ret := m.ctrl.Call(m, "Get", instanceID)
	ret0, _ := ret[0].(dao.MicroGateway)
	ret1, _ := ret[1].(error)
	return ret0, ret1
}

// Get indicates an expected call of Get.
func (mr *MockMicroGatewayManagerMockRecorder) Get(instanceID interface{}) *gomock.Call {
	mr.mock.ctrl.T.Helper()
	return mr.mock.ctrl.RecordCallWithMethodType(mr.mock, "Get", reflect.TypeOf((*MockMicroGatewayManager)(nil).Get), instanceID)
}
