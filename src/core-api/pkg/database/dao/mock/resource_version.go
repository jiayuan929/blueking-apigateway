// Code generated by MockGen. DO NOT EDIT.
// Source: resource_version.go

// Package mock is a generated GoMock package.
package mock

import (
	dao "core/pkg/database/dao"
	reflect "reflect"

	gomock "github.com/golang/mock/gomock"
)

// MockResourceVersionManager is a mock of ResourceVersionManager interface.
type MockResourceVersionManager struct {
	ctrl     *gomock.Controller
	recorder *MockResourceVersionManagerMockRecorder
}

// MockResourceVersionManagerMockRecorder is the mock recorder for MockResourceVersionManager.
type MockResourceVersionManagerMockRecorder struct {
	mock *MockResourceVersionManager
}

// NewMockResourceVersionManager creates a new mock instance.
func NewMockResourceVersionManager(ctrl *gomock.Controller) *MockResourceVersionManager {
	mock := &MockResourceVersionManager{ctrl: ctrl}
	mock.recorder = &MockResourceVersionManagerMockRecorder{mock}
	return mock
}

// EXPECT returns an object that allows the caller to indicate expected use.
func (m *MockResourceVersionManager) EXPECT() *MockResourceVersionManagerMockRecorder {
	return m.recorder
}

// Get mocks base method.
func (m *MockResourceVersionManager) Get(id int64) (dao.ResourceVersion, error) {
	m.ctrl.T.Helper()
	ret := m.ctrl.Call(m, "Get", id)
	ret0, _ := ret[0].(dao.ResourceVersion)
	ret1, _ := ret[1].(error)
	return ret0, ret1
}

// Get indicates an expected call of Get.
func (mr *MockResourceVersionManagerMockRecorder) Get(id interface{}) *gomock.Call {
	mr.mock.ctrl.T.Helper()
	return mr.mock.ctrl.RecordCallWithMethodType(mr.mock, "Get", reflect.TypeOf((*MockResourceVersionManager)(nil).Get), id)
}