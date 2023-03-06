# This Python file uses the following encoding: utf-8
#############################################################################
##
## Copyright (C) 2018 The Qt Company Ltd.
## Contact: https://www.qt.io/licensing/
##
## This file is part of Qt for Python.
##
## $QT_BEGIN_LICENSE:LGPL$
## Commercial License Usage
## Licensees holding valid commercial Qt licenses may use this file in
## accordance with the commercial license agreement provided with the
## Software or, alternatively, in accordance with the terms contained in
## a written agreement between you and The Qt Company. For licensing terms
## and conditions see https://www.qt.io/terms-conditions. For further
## information use the contact form at https://www.qt.io/contact-us.
##
## GNU Lesser General Public License Usage
## Alternatively, this file may be used under the terms of the GNU Lesser
## General Public License version 3 as published by the Free Software
## Foundation and appearing in the file LICENSE.LGPL3 included in the
## packaging of this file. Please review the following information to
## ensure the GNU Lesser General Public License version 3 requirements
## will be met: https://www.gnu.org/licenses/lgpl-3.0.html.
##
## GNU General Public License Usage
## Alternatively, this file may be used under the terms of the GNU
## General Public License version 2.0 or (at your option) the GNU General
## Public license version 3 or any later version approved by the KDE Free
## Qt Foundation. The licenses are as published by the Free Software
## Foundation and appearing in the file LICENSE.GPL2 and LICENSE.GPL3
## included in the packaging of this file. Please review the following
## information to ensure the GNU General Public License requirements will
## be met: https://www.gnu.org/licenses/gpl-2.0.html and
## https://www.gnu.org/licenses/gpl-3.0.html.
##
## $QT_END_LICENSE$
##
#############################################################################

"""
This file contains the exact signatures for all functions in module
PySide2.QtSql, except for defaults which are replaced by "...".
"""

# Module PySide2.QtSql
import shiboken2 as Shiboken
from PySide2.support.signature import typing
from PySide2.support.signature.mapping import (
    Virtual, Missing, Invalid, Default, Instance)

class Object(object): pass

Shiboken.Object = Object

import PySide2.QtCore
import PySide2.QtWidgets
import PySide2.QtSql


class QSql: ...


class QSqlDatabase(Shiboken.Object):

    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, driver:PySide2.QtSql.QSqlDriver): ...
    @typing.overload
    def __init__(self, other:PySide2.QtSql.QSqlDatabase): ...
    @typing.overload
    def __init__(self, type:str): ...
    def __copy__(self): ...
    @typing.overload
    @staticmethod
    def addDatabase(driver:PySide2.QtSql.QSqlDriver, connectionName:str=...) -> PySide2.QtSql.QSqlDatabase: ...
    @typing.overload
    @staticmethod
    def addDatabase(type:str, connectionName:str=...) -> PySide2.QtSql.QSqlDatabase: ...
    @staticmethod
    def cloneDatabase(other:PySide2.QtSql.QSqlDatabase, connectionName:str) -> PySide2.QtSql.QSqlDatabase: ...
    def close(self): ...
    def commit(self) -> bool: ...
    def connectOptions(self) -> str: ...
    def connectionName(self) -> str: ...
    @staticmethod
    def connectionNames() -> typing.List: ...
    @staticmethod
    def contains(connectionName:str=...) -> bool: ...
    @staticmethod
    def database(connectionName:str=..., open:bool=...) -> PySide2.QtSql.QSqlDatabase: ...
    def databaseName(self) -> str: ...
    def driver(self) -> PySide2.QtSql.QSqlDriver: ...
    def driverName(self) -> str: ...
    @staticmethod
    def drivers() -> typing.List: ...
    def exec_(self, query:str=...) -> PySide2.QtSql.QSqlQuery: ...
    def hostName(self) -> str: ...
    @staticmethod
    def isDriverAvailable(name:str) -> bool: ...
    def isOpen(self) -> bool: ...
    def isOpenError(self) -> bool: ...
    def isValid(self) -> bool: ...
    def lastError(self) -> PySide2.QtSql.QSqlError: ...
    def numericalPrecisionPolicy(self) -> PySide2.QtSql.QSql.NumericalPrecisionPolicy: ...
    @typing.overload
    def open(self) -> bool: ...
    @typing.overload
    def open(self, user:str, password:str) -> bool: ...
    def password(self) -> str: ...
    def port(self) -> int: ...
    def primaryIndex(self, tablename:str) -> PySide2.QtSql.QSqlIndex: ...
    def record(self, tablename:str) -> PySide2.QtSql.QSqlRecord: ...
    @staticmethod
    def registerSqlDriver(name:str, creator:PySide2.QtSql.QSqlDriverCreatorBase): ...
    @staticmethod
    def removeDatabase(connectionName:str): ...
    def rollback(self) -> bool: ...
    def setConnectOptions(self, options:str=...): ...
    def setDatabaseName(self, name:str): ...
    def setHostName(self, host:str): ...
    def setNumericalPrecisionPolicy(self, precisionPolicy:PySide2.QtSql.QSql.NumericalPrecisionPolicy): ...
    def setPassword(self, password:str): ...
    def setPort(self, p:int): ...
    def setUserName(self, name:str): ...
    def tables(self, type:PySide2.QtSql.QSql.TableType=...) -> typing.List: ...
    def transaction(self) -> bool: ...
    def userName(self) -> str: ...


class QSqlDriver(PySide2.QtCore.QObject):

    def __init__(self, parent:PySide2.QtCore.QObject=...): ...
    def beginTransaction(self) -> bool: ...
    def cancelQuery(self) -> bool: ...
    def close(self): ...
    def commitTransaction(self) -> bool: ...
    def createResult(self) -> PySide2.QtSql.QSqlResult: ...
    def dbmsType(self) -> PySide2.QtSql.QSqlDriver.DbmsType: ...
    def escapeIdentifier(self, identifier:str, type:PySide2.QtSql.QSqlDriver.IdentifierType) -> str: ...
    def formatValue(self, field:PySide2.QtSql.QSqlField, trimStrings:bool=...) -> str: ...
    def hasFeature(self, f:PySide2.QtSql.QSqlDriver.DriverFeature) -> bool: ...
    def isIdentifierEscaped(self, identifier:str, type:PySide2.QtSql.QSqlDriver.IdentifierType) -> bool: ...
    def isOpen(self) -> bool: ...
    def isOpenError(self) -> bool: ...
    def lastError(self) -> PySide2.QtSql.QSqlError: ...
    def numericalPrecisionPolicy(self) -> PySide2.QtSql.QSql.NumericalPrecisionPolicy: ...
    def open(self, db:str, user:str=..., password:str=..., host:str=..., port:int=..., connOpts:str=...) -> bool: ...
    def primaryIndex(self, tableName:str) -> PySide2.QtSql.QSqlIndex: ...
    def record(self, tableName:str) -> PySide2.QtSql.QSqlRecord: ...
    def rollbackTransaction(self) -> bool: ...
    def setLastError(self, e:PySide2.QtSql.QSqlError): ...
    def setNumericalPrecisionPolicy(self, precisionPolicy:PySide2.QtSql.QSql.NumericalPrecisionPolicy): ...
    def setOpen(self, o:bool): ...
    def setOpenError(self, e:bool): ...
    def sqlStatement(self, type:PySide2.QtSql.QSqlDriver.StatementType, tableName:str, rec:PySide2.QtSql.QSqlRecord, preparedStatement:bool) -> str: ...
    def stripDelimiters(self, identifier:str, type:PySide2.QtSql.QSqlDriver.IdentifierType) -> str: ...
    def subscribeToNotification(self, name:str) -> bool: ...
    def subscribedToNotifications(self) -> typing.List: ...
    def tables(self, tableType:PySide2.QtSql.QSql.TableType) -> typing.List: ...
    def unsubscribeFromNotification(self, name:str) -> bool: ...


class QSqlDriverCreatorBase(Shiboken.Object):

    def __init__(self): ...
    def createObject(self) -> PySide2.QtSql.QSqlDriver: ...


class QSqlError(Shiboken.Object):

    @typing.overload
    def __init__(self, driverText:str, databaseText:str, type:PySide2.QtSql.QSqlError.ErrorType, number:int): ...
    @typing.overload
    def __init__(self, driverText:str=..., databaseText:str=..., type:PySide2.QtSql.QSqlError.ErrorType=..., errorCode:str=...): ...
    @typing.overload
    def __init__(self, other:PySide2.QtSql.QSqlError): ...
    def __copy__(self): ...
    def databaseText(self) -> str: ...
    def driverText(self) -> str: ...
    def isValid(self) -> bool: ...
    def nativeErrorCode(self) -> str: ...
    def number(self) -> int: ...
    def setDatabaseText(self, databaseText:str): ...
    def setDriverText(self, driverText:str): ...
    def setNumber(self, number:int): ...
    def setType(self, type:PySide2.QtSql.QSqlError.ErrorType): ...
    def swap(self, other:PySide2.QtSql.QSqlError): ...
    def text(self) -> str: ...
    def type(self) -> PySide2.QtSql.QSqlError.ErrorType: ...


class QSqlField(Shiboken.Object):

    @typing.overload
    def __init__(self, fieldName:str, type:type, tableName:str): ...
    @typing.overload
    def __init__(self, fieldName:str=..., type:type=...): ...
    @typing.overload
    def __init__(self, other:PySide2.QtSql.QSqlField): ...
    def __copy__(self): ...
    def clear(self): ...
    def defaultValue(self) -> typing.Any: ...
    def isAutoValue(self) -> bool: ...
    def isGenerated(self) -> bool: ...
    def isNull(self) -> bool: ...
    def isReadOnly(self) -> bool: ...
    def isValid(self) -> bool: ...
    def length(self) -> int: ...
    def name(self) -> str: ...
    def precision(self) -> int: ...
    def requiredStatus(self) -> PySide2.QtSql.QSqlField.RequiredStatus: ...
    def setAutoValue(self, autoVal:bool): ...
    def setDefaultValue(self, value:typing.Any): ...
    def setGenerated(self, gen:bool): ...
    def setLength(self, fieldLength:int): ...
    def setName(self, name:str): ...
    def setPrecision(self, precision:int): ...
    def setReadOnly(self, readOnly:bool): ...
    def setRequired(self, required:bool): ...
    def setRequiredStatus(self, status:PySide2.QtSql.QSqlField.RequiredStatus): ...
    def setSqlType(self, type:int): ...
    def setTableName(self, tableName:str): ...
    def setType(self, type:type): ...
    def setValue(self, value:typing.Any): ...
    def tableName(self) -> str: ...
    def type(self) -> type: ...
    def typeID(self) -> int: ...
    def value(self) -> typing.Any: ...


class QSqlIndex(PySide2.QtSql.QSqlRecord):

    @typing.overload
    def __init__(self, cursorName:str=..., name:str=...): ...
    @typing.overload
    def __init__(self, other:PySide2.QtSql.QSqlIndex): ...
    def __copy__(self): ...
    @typing.overload
    def append(self, field:PySide2.QtSql.QSqlField): ...
    @typing.overload
    def append(self, field:PySide2.QtSql.QSqlField, desc:bool): ...
    def cursorName(self) -> str: ...
    def isDescending(self, i:int) -> bool: ...
    def name(self) -> str: ...
    def setCursorName(self, cursorName:str): ...
    def setDescending(self, i:int, desc:bool): ...
    def setName(self, name:str): ...


class QSqlQuery(Shiboken.Object):

    @typing.overload
    def __init__(self, db:PySide2.QtSql.QSqlDatabase): ...
    @typing.overload
    def __init__(self, other:PySide2.QtSql.QSqlQuery): ...
    @typing.overload
    def __init__(self, query:str=..., db:PySide2.QtSql.QSqlDatabase=...): ...
    @typing.overload
    def __init__(self, r:PySide2.QtSql.QSqlResult): ...
    def __copy__(self): ...
    def addBindValue(self, val:typing.Any, type:PySide2.QtSql.QSql.ParamType=...): ...
    def at(self) -> int: ...
    @typing.overload
    def bindValue(self, placeholder:str, val:typing.Any, type:PySide2.QtSql.QSql.ParamType=...): ...
    @typing.overload
    def bindValue(self, pos:int, val:typing.Any, type:PySide2.QtSql.QSql.ParamType=...): ...
    @typing.overload
    def boundValue(self, placeholder:str) -> typing.Any: ...
    @typing.overload
    def boundValue(self, pos:int) -> typing.Any: ...
    def boundValues(self) -> dict: ...
    def clear(self): ...
    def driver(self) -> PySide2.QtSql.QSqlDriver: ...
    def execBatch(self, mode:PySide2.QtSql.QSqlQuery.BatchExecutionMode=...) -> bool: ...
    @typing.overload
    def exec_(self) -> bool: ...
    @typing.overload
    def exec_(self, query:str) -> bool: ...
    def executedQuery(self) -> str: ...
    def finish(self): ...
    def first(self) -> bool: ...
    def isActive(self) -> bool: ...
    def isForwardOnly(self) -> bool: ...
    @typing.overload
    def isNull(self, field:int) -> bool: ...
    @typing.overload
    def isNull(self, name:str) -> bool: ...
    def isSelect(self) -> bool: ...
    def isValid(self) -> bool: ...
    def last(self) -> bool: ...
    def lastError(self) -> PySide2.QtSql.QSqlError: ...
    def lastInsertId(self) -> typing.Any: ...
    def lastQuery(self) -> str: ...
    def next(self) -> bool: ...
    def nextResult(self) -> bool: ...
    def numRowsAffected(self) -> int: ...
    def numericalPrecisionPolicy(self) -> PySide2.QtSql.QSql.NumericalPrecisionPolicy: ...
    def prepare(self, query:str) -> bool: ...
    def previous(self) -> bool: ...
    def record(self) -> PySide2.QtSql.QSqlRecord: ...
    def result(self) -> PySide2.QtSql.QSqlResult: ...
    def seek(self, i:int, relative:bool=...) -> bool: ...
    def setForwardOnly(self, forward:bool): ...
    def setNumericalPrecisionPolicy(self, precisionPolicy:PySide2.QtSql.QSql.NumericalPrecisionPolicy): ...
    def size(self) -> int: ...
    @typing.overload
    def value(self, i:int) -> typing.Any: ...
    @typing.overload
    def value(self, name:str) -> typing.Any: ...


class QSqlQueryModel(PySide2.QtCore.QAbstractTableModel):

    def __init__(self, parent:PySide2.QtCore.QObject=...): ...
    def beginInsertColumns(self, parent:PySide2.QtCore.QModelIndex, first:int, last:int): ...
    def beginInsertRows(self, parent:PySide2.QtCore.QModelIndex, first:int, last:int): ...
    def beginRemoveColumns(self, parent:PySide2.QtCore.QModelIndex, first:int, last:int): ...
    def beginRemoveRows(self, parent:PySide2.QtCore.QModelIndex, first:int, last:int): ...
    def beginResetModel(self): ...
    def canFetchMore(self, parent:PySide2.QtCore.QModelIndex=...) -> bool: ...
    def clear(self): ...
    def columnCount(self, parent:PySide2.QtCore.QModelIndex=...) -> int: ...
    def data(self, item:PySide2.QtCore.QModelIndex, role:int=...) -> typing.Any: ...
    def endInsertColumns(self): ...
    def endInsertRows(self): ...
    def endRemoveColumns(self): ...
    def endRemoveRows(self): ...
    def endResetModel(self): ...
    def fetchMore(self, parent:PySide2.QtCore.QModelIndex=...): ...
    def headerData(self, section:int, orientation:PySide2.QtCore.Qt.Orientation, role:int=...) -> typing.Any: ...
    def indexInQuery(self, item:PySide2.QtCore.QModelIndex) -> PySide2.QtCore.QModelIndex: ...
    def insertColumns(self, column:int, count:int, parent:PySide2.QtCore.QModelIndex=...) -> bool: ...
    def lastError(self) -> PySide2.QtSql.QSqlError: ...
    def query(self) -> PySide2.QtSql.QSqlQuery: ...
    def queryChange(self): ...
    @typing.overload
    def record(self) -> PySide2.QtSql.QSqlRecord: ...
    @typing.overload
    def record(self, row:int) -> PySide2.QtSql.QSqlRecord: ...
    def removeColumns(self, column:int, count:int, parent:PySide2.QtCore.QModelIndex=...) -> bool: ...
    def roleNames(self) -> dict: ...
    def rowCount(self, parent:PySide2.QtCore.QModelIndex=...) -> int: ...
    def setHeaderData(self, section:int, orientation:PySide2.QtCore.Qt.Orientation, value:typing.Any, role:int=...) -> bool: ...
    def setLastError(self, error:PySide2.QtSql.QSqlError): ...
    @typing.overload
    def setQuery(self, query:PySide2.QtSql.QSqlQuery): ...
    @typing.overload
    def setQuery(self, query:str, db:PySide2.QtSql.QSqlDatabase=...): ...


class QSqlRecord(Shiboken.Object):

    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, other:PySide2.QtSql.QSqlRecord): ...
    def __copy__(self): ...
    def append(self, field:PySide2.QtSql.QSqlField): ...
    def clear(self): ...
    def clearValues(self): ...
    def contains(self, name:str) -> bool: ...
    def count(self) -> int: ...
    @typing.overload
    def field(self, i:int) -> PySide2.QtSql.QSqlField: ...
    @typing.overload
    def field(self, name:str) -> PySide2.QtSql.QSqlField: ...
    def fieldName(self, i:int) -> str: ...
    def indexOf(self, name:str) -> int: ...
    def insert(self, pos:int, field:PySide2.QtSql.QSqlField): ...
    def isEmpty(self) -> bool: ...
    @typing.overload
    def isGenerated(self, i:int) -> bool: ...
    @typing.overload
    def isGenerated(self, name:str) -> bool: ...
    @typing.overload
    def isNull(self, i:int) -> bool: ...
    @typing.overload
    def isNull(self, name:str) -> bool: ...
    def keyValues(self, keyFields:PySide2.QtSql.QSqlRecord) -> PySide2.QtSql.QSqlRecord: ...
    def remove(self, pos:int): ...
    def replace(self, pos:int, field:PySide2.QtSql.QSqlField): ...
    @typing.overload
    def setGenerated(self, i:int, generated:bool): ...
    @typing.overload
    def setGenerated(self, name:str, generated:bool): ...
    @typing.overload
    def setNull(self, i:int): ...
    @typing.overload
    def setNull(self, name:str): ...
    @typing.overload
    def setValue(self, i:int, val:typing.Any): ...
    @typing.overload
    def setValue(self, name:str, val:typing.Any): ...
    @typing.overload
    def value(self, i:int) -> typing.Any: ...
    @typing.overload
    def value(self, name:str) -> typing.Any: ...


class QSqlRelation(Shiboken.Object):

    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, QSqlRelation:PySide2.QtSql.QSqlRelation): ...
    @typing.overload
    def __init__(self, aTableName:str, indexCol:str, displayCol:str): ...
    def __copy__(self): ...
    def displayColumn(self) -> str: ...
    def indexColumn(self) -> str: ...
    def isValid(self) -> bool: ...
    def swap(self, other:PySide2.QtSql.QSqlRelation): ...
    def tableName(self) -> str: ...


class QSqlRelationalDelegate(PySide2.QtWidgets.QItemDelegate):

    def __init__(self, aParent:PySide2.QtCore.QObject=...): ...
    def createEditor(self, aParent:PySide2.QtWidgets.QWidget, option:PySide2.QtWidgets.QStyleOptionViewItem, index:PySide2.QtCore.QModelIndex) -> PySide2.QtWidgets.QWidget: ...
    def setEditorData(self, editor:PySide2.QtWidgets.QWidget, index:PySide2.QtCore.QModelIndex): ...
    def setModelData(self, editor:PySide2.QtWidgets.QWidget, model:PySide2.QtCore.QAbstractItemModel, index:PySide2.QtCore.QModelIndex): ...


class QSqlRelationalTableModel(PySide2.QtSql.QSqlTableModel):

    def __init__(self, parent:PySide2.QtCore.QObject=..., db:PySide2.QtSql.QSqlDatabase=...): ...
    def clear(self): ...
    def data(self, item:PySide2.QtCore.QModelIndex, role:int=...) -> typing.Any: ...
    def insertRowIntoTable(self, values:PySide2.QtSql.QSqlRecord) -> bool: ...
    def orderByClause(self) -> str: ...
    def relation(self, column:int) -> PySide2.QtSql.QSqlRelation: ...
    def relationModel(self, column:int) -> PySide2.QtSql.QSqlTableModel: ...
    def removeColumns(self, column:int, count:int, parent:PySide2.QtCore.QModelIndex=...) -> bool: ...
    def revertRow(self, row:int): ...
    def select(self) -> bool: ...
    def selectStatement(self) -> str: ...
    def setData(self, item:PySide2.QtCore.QModelIndex, value:typing.Any, role:int=...) -> bool: ...
    def setJoinMode(self, joinMode:PySide2.QtSql.QSqlRelationalTableModel.JoinMode): ...
    def setRelation(self, column:int, relation:PySide2.QtSql.QSqlRelation): ...
    def setTable(self, tableName:str): ...
    def updateRowInTable(self, row:int, values:PySide2.QtSql.QSqlRecord) -> bool: ...


class QSqlResult(Shiboken.Object):

    def __init__(self, db:PySide2.QtSql.QSqlDriver): ...
    def addBindValue(self, val:typing.Any, type:PySide2.QtSql.QSql.ParamType): ...
    def at(self) -> int: ...
    @typing.overload
    def bindValue(self, placeholder:str, val:typing.Any, type:PySide2.QtSql.QSql.ParamType): ...
    @typing.overload
    def bindValue(self, pos:int, val:typing.Any, type:PySide2.QtSql.QSql.ParamType): ...
    @typing.overload
    def bindValueType(self, placeholder:str) -> PySide2.QtSql.QSql.ParamType: ...
    @typing.overload
    def bindValueType(self, pos:int) -> PySide2.QtSql.QSql.ParamType: ...
    def bindingSyntax(self) -> PySide2.QtSql.QSqlResult.BindingSyntax: ...
    @typing.overload
    def boundValue(self, placeholder:str) -> typing.Any: ...
    @typing.overload
    def boundValue(self, pos:int) -> typing.Any: ...
    def boundValueCount(self) -> int: ...
    def boundValueName(self, pos:int) -> str: ...
    def boundValues(self) -> typing.Any: ...
    def clear(self): ...
    def data(self, i:int) -> typing.Any: ...
    def detachFromResultSet(self): ...
    def driver(self) -> PySide2.QtSql.QSqlDriver: ...
    def execBatch(self, arrayBind:bool=...) -> bool: ...
    def exec_(self) -> bool: ...
    def executedQuery(self) -> str: ...
    def fetch(self, i:int) -> bool: ...
    def fetchFirst(self) -> bool: ...
    def fetchLast(self) -> bool: ...
    def fetchNext(self) -> bool: ...
    def fetchPrevious(self) -> bool: ...
    def handle(self) -> typing.Any: ...
    def hasOutValues(self) -> bool: ...
    def isActive(self) -> bool: ...
    def isForwardOnly(self) -> bool: ...
    def isNull(self, i:int) -> bool: ...
    def isSelect(self) -> bool: ...
    def isValid(self) -> bool: ...
    def lastError(self) -> PySide2.QtSql.QSqlError: ...
    def lastInsertId(self) -> typing.Any: ...
    def lastQuery(self) -> str: ...
    def nextResult(self) -> bool: ...
    def numRowsAffected(self) -> int: ...
    def numericalPrecisionPolicy(self) -> PySide2.QtSql.QSql.NumericalPrecisionPolicy: ...
    def prepare(self, query:str) -> bool: ...
    def record(self) -> PySide2.QtSql.QSqlRecord: ...
    def reset(self, sqlquery:str) -> bool: ...
    def resetBindCount(self): ...
    def savePrepare(self, sqlquery:str) -> bool: ...
    def setActive(self, a:bool): ...
    def setAt(self, at:int): ...
    def setForwardOnly(self, forward:bool): ...
    def setLastError(self, e:PySide2.QtSql.QSqlError): ...
    def setNumericalPrecisionPolicy(self, policy:PySide2.QtSql.QSql.NumericalPrecisionPolicy): ...
    def setQuery(self, query:str): ...
    def setSelect(self, s:bool): ...
    def size(self) -> int: ...


class QSqlTableModel(PySide2.QtSql.QSqlQueryModel):

    def __init__(self, parent:PySide2.QtCore.QObject=..., db:PySide2.QtSql.QSqlDatabase=...): ...
    def clear(self): ...
    def data(self, idx:PySide2.QtCore.QModelIndex, role:int=...) -> typing.Any: ...
    def database(self) -> PySide2.QtSql.QSqlDatabase: ...
    def deleteRowFromTable(self, row:int) -> bool: ...
    def editStrategy(self) -> PySide2.QtSql.QSqlTableModel.EditStrategy: ...
    def fieldIndex(self, fieldName:str) -> int: ...
    def filter(self) -> str: ...
    def flags(self, index:PySide2.QtCore.QModelIndex) -> PySide2.QtCore.Qt.ItemFlags: ...
    def headerData(self, section:int, orientation:PySide2.QtCore.Qt.Orientation, role:int=...) -> typing.Any: ...
    def indexInQuery(self, item:PySide2.QtCore.QModelIndex) -> PySide2.QtCore.QModelIndex: ...
    def insertRecord(self, row:int, record:PySide2.QtSql.QSqlRecord) -> bool: ...
    def insertRowIntoTable(self, values:PySide2.QtSql.QSqlRecord) -> bool: ...
    def insertRows(self, row:int, count:int, parent:PySide2.QtCore.QModelIndex=...) -> bool: ...
    @typing.overload
    def isDirty(self) -> bool: ...
    @typing.overload
    def isDirty(self, index:PySide2.QtCore.QModelIndex) -> bool: ...
    def orderByClause(self) -> str: ...
    def primaryKey(self) -> PySide2.QtSql.QSqlIndex: ...
    def primaryValues(self, row:int) -> PySide2.QtSql.QSqlRecord: ...
    @typing.overload
    def record(self) -> PySide2.QtSql.QSqlRecord: ...
    @typing.overload
    def record(self, row:int) -> PySide2.QtSql.QSqlRecord: ...
    def removeColumns(self, column:int, count:int, parent:PySide2.QtCore.QModelIndex=...) -> bool: ...
    def removeRows(self, row:int, count:int, parent:PySide2.QtCore.QModelIndex=...) -> bool: ...
    def revert(self): ...
    def revertAll(self): ...
    def revertRow(self, row:int): ...
    def rowCount(self, parent:PySide2.QtCore.QModelIndex=...) -> int: ...
    def select(self) -> bool: ...
    def selectRow(self, row:int) -> bool: ...
    def selectStatement(self) -> str: ...
    def setData(self, index:PySide2.QtCore.QModelIndex, value:typing.Any, role:int=...) -> bool: ...
    def setEditStrategy(self, strategy:PySide2.QtSql.QSqlTableModel.EditStrategy): ...
    def setFilter(self, filter:str): ...
    def setPrimaryKey(self, key:PySide2.QtSql.QSqlIndex): ...
    def setQuery(self, query:PySide2.QtSql.QSqlQuery): ...
    def setRecord(self, row:int, record:PySide2.QtSql.QSqlRecord) -> bool: ...
    def setSort(self, column:int, order:PySide2.QtCore.Qt.SortOrder): ...
    def setTable(self, tableName:str): ...
    def sort(self, column:int, order:PySide2.QtCore.Qt.SortOrder): ...
    def submit(self) -> bool: ...
    def submitAll(self) -> bool: ...
    def tableName(self) -> str: ...
    def updateRowInTable(self, row:int, values:PySide2.QtSql.QSqlRecord) -> bool: ...

# eof
