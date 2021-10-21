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
PySide2.Qt3DCore, except for defaults which are replaced by "...".
"""

# Module PySide2.Qt3DCore
import shiboken2 as Shiboken
from PySide2.support.signature import typing
from PySide2.support.signature.mapping import (
    Virtual, Missing, Invalid, Default, Instance)

class Object(object): pass

Shiboken.Object = Object

import PySide2.QtCore
import PySide2.QtGui
import PySide2.Qt3DCore


class Qt3DCore(Shiboken.Object):

    @staticmethod
    def qHash(id:PySide2.Qt3DCore.Qt3DCore.QNodeId, seed:int=...) -> int: ...
    @staticmethod
    def qIdForNode(node:PySide2.Qt3DCore.Qt3DCore.QNode) -> PySide2.Qt3DCore.Qt3DCore.QNodeId: ...

    class QAbstractAspect(PySide2.QtCore.QObject):

        def __init__(self, parent:PySide2.QtCore.QObject=...): ...
        def rootEntityId(self) -> PySide2.Qt3DCore.Qt3DCore.QNodeId: ...
        def unregisterBackendType(self, arg__1:PySide2.QtCore.QMetaObject): ...

    class QAbstractSkeleton(PySide2.Qt3DCore.Qt3DCore.QNode):

        def jointCount(self) -> int: ...

    class QArmature(PySide2.Qt3DCore.Qt3DCore.QComponent):

        def __init__(self, parent:PySide2.Qt3DCore.Qt3DCore.QNode=...): ...
        def setSkeleton(self, skeleton:PySide2.Qt3DCore.Qt3DCore.QAbstractSkeleton): ...
        def skeleton(self) -> PySide2.Qt3DCore.Qt3DCore.QAbstractSkeleton: ...

    class QAspectEngine(PySide2.QtCore.QObject):

        def __init__(self, parent:PySide2.QtCore.QObject=...): ...
        def aspects(self) -> PySide2.Qt3DCore.Qt3DCore.QAbstractAspect: ...
        def executeCommand(self, command:str) -> typing.Any: ...
        @typing.overload
        def registerAspect(self, aspect:PySide2.Qt3DCore.Qt3DCore.QAbstractAspect): ...
        @typing.overload
        def registerAspect(self, name:str): ...
        @typing.overload
        def unregisterAspect(self, aspect:PySide2.Qt3DCore.Qt3DCore.QAbstractAspect): ...
        @typing.overload
        def unregisterAspect(self, name:str): ...

    class QAspectJob(Shiboken.Object):

        def __init__(self): ...
        def run(self): ...

    class QBackendNode(Shiboken.Object):

        def __init__(self, mode:PySide2.Qt3DCore.Qt3DCore.QBackendNode.Mode=...): ...
        def isEnabled(self) -> bool: ...
        def mode(self) -> PySide2.Qt3DCore.Qt3DCore.QBackendNode.Mode: ...
        def peerId(self) -> PySide2.Qt3DCore.Qt3DCore.QNodeId: ...
        def setEnabled(self, enabled:bool): ...

    class QComponent(PySide2.Qt3DCore.Qt3DCore.QNode):

        def __init__(self, parent:PySide2.Qt3DCore.Qt3DCore.QNode=...): ...
        def entities(self) -> PySide2.Qt3DCore.Qt3DCore.QEntity: ...
        def isShareable(self) -> bool: ...
        def setShareable(self, isShareable:bool): ...

    class QComponentAddedChange(PySide2.Qt3DCore.Qt3DCore.QSceneChange):

        @typing.overload
        def __init__(self, component:PySide2.Qt3DCore.Qt3DCore.QComponent, entity:PySide2.Qt3DCore.Qt3DCore.QEntity): ...
        @typing.overload
        def __init__(self, entity:PySide2.Qt3DCore.Qt3DCore.QEntity, component:PySide2.Qt3DCore.Qt3DCore.QComponent): ...
        def componentId(self) -> PySide2.Qt3DCore.Qt3DCore.QNodeId: ...
        def componentMetaObject(self) -> PySide2.QtCore.QMetaObject: ...
        def entityId(self) -> PySide2.Qt3DCore.Qt3DCore.QNodeId: ...

    class QComponentRemovedChange(PySide2.Qt3DCore.Qt3DCore.QSceneChange):

        @typing.overload
        def __init__(self, component:PySide2.Qt3DCore.Qt3DCore.QComponent, entity:PySide2.Qt3DCore.Qt3DCore.QEntity): ...
        @typing.overload
        def __init__(self, entity:PySide2.Qt3DCore.Qt3DCore.QEntity, component:PySide2.Qt3DCore.Qt3DCore.QComponent): ...
        def componentId(self) -> PySide2.Qt3DCore.Qt3DCore.QNodeId: ...
        def componentMetaObject(self) -> PySide2.QtCore.QMetaObject: ...
        def entityId(self) -> PySide2.Qt3DCore.Qt3DCore.QNodeId: ...

    class QDynamicPropertyUpdatedChange(PySide2.Qt3DCore.Qt3DCore.QPropertyUpdatedChangeBase):

        def __init__(self, subjectId:PySide2.Qt3DCore.Qt3DCore.QNodeId): ...
        def propertyName(self) -> PySide2.QtCore.QByteArray: ...
        def setPropertyName(self, name:PySide2.QtCore.QByteArray): ...
        def setValue(self, value:typing.Any): ...
        def value(self) -> typing.Any: ...

    class QEntity(PySide2.Qt3DCore.Qt3DCore.QNode):

        def __init__(self, parent:PySide2.Qt3DCore.Qt3DCore.QNode=...): ...
        def addComponent(self, comp:PySide2.Qt3DCore.Qt3DCore.QComponent): ...
        def components(self) -> PySide2.Qt3DCore.Qt3DCore.QComponent: ...
        def parentEntity(self) -> PySide2.Qt3DCore.Qt3DCore.QEntity: ...
        def removeComponent(self, comp:PySide2.Qt3DCore.Qt3DCore.QComponent): ...

    class QJoint(PySide2.Qt3DCore.Qt3DCore.QNode):

        def __init__(self, parent:PySide2.Qt3DCore.Qt3DCore.QNode=...): ...
        def addChildJoint(self, joint:PySide2.Qt3DCore.Qt3DCore.QJoint): ...
        def childJoints(self) -> PySide2.Qt3DCore.Qt3DCore.QJoint: ...
        def inverseBindMatrix(self) -> PySide2.QtGui.QMatrix4x4: ...
        def name(self) -> str: ...
        def removeChildJoint(self, joint:PySide2.Qt3DCore.Qt3DCore.QJoint): ...
        def rotation(self) -> PySide2.QtGui.QQuaternion: ...
        def rotationX(self) -> float: ...
        def rotationY(self) -> float: ...
        def rotationZ(self) -> float: ...
        def scale(self) -> PySide2.QtGui.QVector3D: ...
        def setInverseBindMatrix(self, inverseBindMatrix:PySide2.QtGui.QMatrix4x4): ...
        def setName(self, name:str): ...
        def setRotation(self, rotation:PySide2.QtGui.QQuaternion): ...
        def setRotationX(self, rotationX:float): ...
        def setRotationY(self, rotationY:float): ...
        def setRotationZ(self, rotationZ:float): ...
        def setScale(self, scale:PySide2.QtGui.QVector3D): ...
        def setToIdentity(self): ...
        def setTranslation(self, translation:PySide2.QtGui.QVector3D): ...
        def translation(self) -> PySide2.QtGui.QVector3D: ...

    class QNode(PySide2.QtCore.QObject):

        def __init__(self, parent:PySide2.Qt3DCore.Qt3DCore.QNode=...): ...
        def blockNotifications(self, block:bool) -> bool: ...
        def childNodes(self) -> PySide2.Qt3DCore.Qt3DCore.QNode: ...
        def clearPropertyTracking(self, propertyName:str): ...
        def clearPropertyTrackings(self): ...
        def defaultPropertyTrackingMode(self) -> PySide2.Qt3DCore.Qt3DCore.QNode.PropertyTrackingMode: ...
        def id(self) -> PySide2.Qt3DCore.Qt3DCore.QNodeId: ...
        def isEnabled(self) -> bool: ...
        def notificationsBlocked(self) -> bool: ...
        def parentNode(self) -> PySide2.Qt3DCore.Qt3DCore.QNode: ...
        def propertyTracking(self, propertyName:str) -> PySide2.Qt3DCore.Qt3DCore.QNode.PropertyTrackingMode: ...
        def setDefaultPropertyTrackingMode(self, mode:PySide2.Qt3DCore.Qt3DCore.QNode.PropertyTrackingMode): ...
        def setEnabled(self, isEnabled:bool): ...
        @typing.overload
        def setParent(self, parent:PySide2.Qt3DCore.Qt3DCore.QNode): ...
        @typing.overload
        def setParent(self, parent:PySide2.QtCore.QObject): ...
        def setPropertyTracking(self, propertyName:str, trackMode:PySide2.Qt3DCore.Qt3DCore.QNode.PropertyTrackingMode): ...

    class QNodeCommand(PySide2.Qt3DCore.Qt3DCore.QSceneChange):

        def __init__(self, id:PySide2.Qt3DCore.Qt3DCore.QNodeId): ...
        def commandId(self) -> int: ...
        def data(self) -> typing.Any: ...
        def inReplyTo(self) -> int: ...
        def name(self) -> str: ...
        def setData(self, data:typing.Any): ...
        def setName(self, name:str): ...
        def setReplyToCommandId(self, id:int): ...

    class QNodeCreatedChangeBase(PySide2.Qt3DCore.Qt3DCore.QSceneChange):

        def __init__(self, node:PySide2.Qt3DCore.Qt3DCore.QNode): ...
        def isNodeEnabled(self) -> bool: ...
        def parentId(self) -> PySide2.Qt3DCore.Qt3DCore.QNodeId: ...

    class QNodeDestroyedChange(PySide2.Qt3DCore.Qt3DCore.QSceneChange):

        def __init__(self, node:PySide2.Qt3DCore.Qt3DCore.QNode, subtreeIdsAndTypes:list): ...
        def subtreeIdsAndTypes(self) -> PySide2.Qt3DCore.Qt3DCore.QNodeIdTypePair: ...

    class QNodeId(Shiboken.Object):

        @typing.overload
        def __init__(self): ...
        @typing.overload
        def __init__(self, QNodeId:PySide2.Qt3DCore.Qt3DCore.QNodeId): ...
        def __copy__(self): ...
        @staticmethod
        def createId() -> PySide2.Qt3DCore.Qt3DCore.QNodeId: ...
        def id(self) -> int: ...
        def isNull(self) -> bool: ...

    class QNodeIdTypePair(Shiboken.Object):

        @typing.overload
        def __init__(self): ...
        @typing.overload
        def __init__(self, QNodeIdTypePair:PySide2.Qt3DCore.Qt3DCore.QNodeIdTypePair): ...
        @typing.overload
        def __init__(self, _id:PySide2.Qt3DCore.Qt3DCore.QNodeId, _type:PySide2.QtCore.QMetaObject): ...
        def __copy__(self): ...

    class QPropertyNodeAddedChange(PySide2.Qt3DCore.Qt3DCore.QStaticPropertyValueAddedChangeBase):

        def __init__(self, subjectId:PySide2.Qt3DCore.Qt3DCore.QNodeId, node:PySide2.Qt3DCore.Qt3DCore.QNode): ...
        def addedNodeId(self) -> PySide2.Qt3DCore.Qt3DCore.QNodeId: ...

    class QPropertyNodeRemovedChange(PySide2.Qt3DCore.Qt3DCore.QStaticPropertyValueRemovedChangeBase):

        def __init__(self, subjectId:PySide2.Qt3DCore.Qt3DCore.QNodeId, node:PySide2.Qt3DCore.Qt3DCore.QNode): ...
        def removedNodeId(self) -> PySide2.Qt3DCore.Qt3DCore.QNodeId: ...

    class QPropertyUpdatedChange(PySide2.Qt3DCore.Qt3DCore.QStaticPropertyUpdatedChangeBase):

        def __init__(self, subjectId:PySide2.Qt3DCore.Qt3DCore.QNodeId): ...
        def setValue(self, value:typing.Any): ...
        def value(self) -> typing.Any: ...

    class QPropertyUpdatedChangeBase(PySide2.Qt3DCore.Qt3DCore.QSceneChange):

        def __init__(self, subjectId:PySide2.Qt3DCore.Qt3DCore.QNodeId): ...

    class QPropertyValueAddedChange(PySide2.Qt3DCore.Qt3DCore.QStaticPropertyValueAddedChangeBase):

        def __init__(self, subjectId:PySide2.Qt3DCore.Qt3DCore.QNodeId): ...
        def addedValue(self) -> typing.Any: ...
        def setAddedValue(self, value:typing.Any): ...

    class QPropertyValueAddedChangeBase(PySide2.Qt3DCore.Qt3DCore.QSceneChange):

        def __init__(self, subjectId:PySide2.Qt3DCore.Qt3DCore.QNodeId): ...

    class QPropertyValueRemovedChange(PySide2.Qt3DCore.Qt3DCore.QStaticPropertyValueRemovedChangeBase):

        def __init__(self, subjectId:PySide2.Qt3DCore.Qt3DCore.QNodeId): ...
        def removedValue(self) -> typing.Any: ...
        def setRemovedValue(self, value:typing.Any): ...

    class QPropertyValueRemovedChangeBase(PySide2.Qt3DCore.Qt3DCore.QSceneChange):

        def __init__(self, subjectId:PySide2.Qt3DCore.Qt3DCore.QNodeId): ...

    class QSceneChange(Shiboken.Object):

        def __init__(self, type:PySide2.Qt3DCore.Qt3DCore.ChangeFlag, subjectId:PySide2.Qt3DCore.Qt3DCore.QNodeId): ...
        def deliveryFlags(self) -> PySide2.Qt3DCore.Qt3DCore.QSceneChange.DeliveryFlags: ...
        def setDeliveryFlags(self, flags:PySide2.Qt3DCore.Qt3DCore.QSceneChange.DeliveryFlags): ...
        def subjectId(self) -> PySide2.Qt3DCore.Qt3DCore.QNodeId: ...
        def type(self) -> PySide2.Qt3DCore.Qt3DCore.ChangeFlag: ...

    class QSkeleton(PySide2.Qt3DCore.Qt3DCore.QAbstractSkeleton):

        def __init__(self, parent:PySide2.Qt3DCore.Qt3DCore.QNode=...): ...
        def rootJoint(self) -> PySide2.Qt3DCore.Qt3DCore.QJoint: ...
        def setRootJoint(self, rootJoint:PySide2.Qt3DCore.Qt3DCore.QJoint): ...

    class QSkeletonLoader(PySide2.Qt3DCore.Qt3DCore.QAbstractSkeleton):

        @typing.overload
        def __init__(self, parent:PySide2.Qt3DCore.Qt3DCore.QNode=...): ...
        @typing.overload
        def __init__(self, source:PySide2.QtCore.QUrl, parent:PySide2.Qt3DCore.Qt3DCore.QNode=...): ...
        def isCreateJointsEnabled(self) -> bool: ...
        def rootJoint(self) -> PySide2.Qt3DCore.Qt3DCore.QJoint: ...
        def setCreateJointsEnabled(self, enabled:bool): ...
        def setSource(self, source:PySide2.QtCore.QUrl): ...
        def source(self) -> PySide2.QtCore.QUrl: ...
        def status(self) -> PySide2.Qt3DCore.Qt3DCore.QSkeletonLoader.Status: ...

    class QStaticPropertyUpdatedChangeBase(PySide2.Qt3DCore.Qt3DCore.QPropertyUpdatedChangeBase):

        def __init__(self, subjectId:PySide2.Qt3DCore.Qt3DCore.QNodeId): ...
        def propertyName(self) -> str: ...
        def setPropertyName(self, name:str): ...

    class QStaticPropertyValueAddedChangeBase(PySide2.Qt3DCore.Qt3DCore.QPropertyValueAddedChangeBase):

        def __init__(self, subjectId:PySide2.Qt3DCore.Qt3DCore.QNodeId): ...
        def propertyName(self) -> str: ...
        def setPropertyName(self, name:str): ...

    class QStaticPropertyValueRemovedChangeBase(PySide2.Qt3DCore.Qt3DCore.QPropertyValueRemovedChangeBase):

        def __init__(self, subjectId:PySide2.Qt3DCore.Qt3DCore.QNodeId): ...
        def propertyName(self) -> str: ...
        def setPropertyName(self, name:str): ...

    class QTransform(PySide2.Qt3DCore.Qt3DCore.QComponent):

        def __init__(self, parent:PySide2.Qt3DCore.Qt3DCore.QNode=...): ...
        @staticmethod
        def fromAxes(xAxis:PySide2.QtGui.QVector3D, yAxis:PySide2.QtGui.QVector3D, zAxis:PySide2.QtGui.QVector3D) -> PySide2.QtGui.QQuaternion: ...
        @typing.overload
        @staticmethod
        def fromAxesAndAngles(axis1:PySide2.QtGui.QVector3D, angle1:float, axis2:PySide2.QtGui.QVector3D, angle2:float) -> PySide2.QtGui.QQuaternion: ...
        @typing.overload
        @staticmethod
        def fromAxesAndAngles(axis1:PySide2.QtGui.QVector3D, angle1:float, axis2:PySide2.QtGui.QVector3D, angle2:float, axis3:PySide2.QtGui.QVector3D, angle3:float) -> PySide2.QtGui.QQuaternion: ...
        @typing.overload
        @staticmethod
        def fromAxisAndAngle(axis:PySide2.QtGui.QVector3D, angle:float) -> PySide2.QtGui.QQuaternion: ...
        @typing.overload
        @staticmethod
        def fromAxisAndAngle(x:float, y:float, z:float, angle:float) -> PySide2.QtGui.QQuaternion: ...
        @typing.overload
        @staticmethod
        def fromEulerAngles(eulerAngles:PySide2.QtGui.QVector3D) -> PySide2.QtGui.QQuaternion: ...
        @typing.overload
        @staticmethod
        def fromEulerAngles(pitch:float, yaw:float, roll:float) -> PySide2.QtGui.QQuaternion: ...
        def matrix(self) -> PySide2.QtGui.QMatrix4x4: ...
        @staticmethod
        def rotateAround(point:PySide2.QtGui.QVector3D, angle:float, axis:PySide2.QtGui.QVector3D) -> PySide2.QtGui.QMatrix4x4: ...
        @staticmethod
        def rotateFromAxes(xAxis:PySide2.QtGui.QVector3D, yAxis:PySide2.QtGui.QVector3D, zAxis:PySide2.QtGui.QVector3D) -> PySide2.QtGui.QMatrix4x4: ...
        def rotation(self) -> PySide2.QtGui.QQuaternion: ...
        def rotationX(self) -> float: ...
        def rotationY(self) -> float: ...
        def rotationZ(self) -> float: ...
        def scale(self) -> float: ...
        def scale3D(self) -> PySide2.QtGui.QVector3D: ...
        def setMatrix(self, matrix:PySide2.QtGui.QMatrix4x4): ...
        def setRotation(self, rotation:PySide2.QtGui.QQuaternion): ...
        def setRotationX(self, rotationX:float): ...
        def setRotationY(self, rotationY:float): ...
        def setRotationZ(self, rotationZ:float): ...
        def setScale(self, scale:float): ...
        def setScale3D(self, scale:PySide2.QtGui.QVector3D): ...
        def setTranslation(self, translation:PySide2.QtGui.QVector3D): ...
        def translation(self) -> PySide2.QtGui.QVector3D: ...

# eof
