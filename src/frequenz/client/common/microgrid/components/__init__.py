# License: MIT
# Copyright © 2022 Frequenz Energy-as-a-Service GmbH

"""Defines the components that can be used in a microgrid."""
from __future__ import annotations

from enum import Enum

# pylint: disable=no-name-in-module
from frequenz.api.common.v1.microgrid.components.components_pb2 import (
    ComponentCategory as PBComponentCategory,
)
from frequenz.api.common.v1.microgrid.components.components_pb2 import (
    ComponentStateCode as PBComponentStateCode,
)

# pylint: enable=no-name-in-module


class ComponentCategory(Enum):
    """Possible types of microgrid component."""

    UNSPECIFIED = PBComponentCategory.COMPONENT_CATEGORY_UNSPECIFIED
    """An unknown component category.

    Useful for error handling, and marking unknown components in
    a list of components with otherwise known categories.
    """

    GRID = PBComponentCategory.COMPONENT_CATEGORY_GRID
    """The point where the local microgrid is connected to the grid."""

    METER = PBComponentCategory.COMPONENT_CATEGORY_METER
    """A meter, for measuring electrical metrics, e.g., current, voltage, etc."""

    INVERTER = PBComponentCategory.COMPONENT_CATEGORY_INVERTER
    """An electricity generator, with batteries or solar energy."""

    BATTERY = PBComponentCategory.COMPONENT_CATEGORY_BATTERY
    """A storage system for electrical energy, used by inverters."""

    EV_CHARGER = PBComponentCategory.COMPONENT_CATEGORY_EV_CHARGER
    """A station for charging electrical vehicles."""

    CHP = PBComponentCategory.COMPONENT_CATEGORY_CHP
    """A heat and power combustion plant (CHP stands for combined heat and power)."""

    @classmethod
    def from_proto(
        cls, component_category: PBComponentCategory.ValueType
    ) -> ComponentCategory:
        """Convert a protobuf ComponentCategory message to ComponentCategory enum.

        Args:
            component_category: protobuf enum to convert

        Returns:
            Enum value corresponding to the protobuf message.
        """
        if not any(t.value == component_category for t in ComponentCategory):
            return ComponentCategory.UNSPECIFIED
        return cls(component_category)

    def to_proto(self) -> PBComponentCategory.ValueType:
        """Convert a ComponentCategory enum to protobuf ComponentCategory message.

        Returns:
            Enum value corresponding to the protobuf message.
        """
        return self.value


class ComponentStateCode(Enum):
    """All possible states of a microgrid component."""

    UNSPECIFIED = PBComponentStateCode.COMPONENT_STATE_CODE_UNSPECIFIED
    """Default value when the component state is not explicitly set."""

    UNKNOWN = PBComponentStateCode.COMPONENT_STATE_CODE_UNKNOWN
    """State when the component is in an unknown or undefined condition.

    This is used when the sender is unable to classify the component into any
    other state.
    """
    SWITCHING_OFF = PBComponentStateCode.COMPONENT_STATE_CODE_SWITCHING_OFF
    """State when the component is in the process of switching off."""

    OFF = PBComponentStateCode.COMPONENT_STATE_CODE_OFF
    """State when the component has successfully switched off."""

    SWITCHING_ON = PBComponentStateCode.COMPONENT_STATE_CODE_SWITCHING_ON
    """State when the component is in the process of switching on from an off state."""

    STANDBY = PBComponentStateCode.COMPONENT_STATE_CODE_STANDBY
    """State when the component is in standby mode, and not immediately ready for operation."""

    READY = PBComponentStateCode.COMPONENT_STATE_CODE_READY
    """State when the component is fully operational and ready for use."""

    CHARGING = PBComponentStateCode.COMPONENT_STATE_CODE_CHARGING
    """State when the component is actively consuming energy."""

    DISCHARGING = PBComponentStateCode.COMPONENT_STATE_CODE_DISCHARGING
    """State when the component is actively producing or releasing energy."""

    ERROR = PBComponentStateCode.COMPONENT_STATE_CODE_ERROR
    """State when the component is in an error state and may need attention."""

    EV_CHARGING_CABLE_UNPLUGGED = (
        PBComponentStateCode.COMPONENT_STATE_CODE_EV_CHARGING_CABLE_UNPLUGGED
    )
    """The Electric Vehicle (EV) charging cable is unplugged from the charging station."""

    EV_CHARGING_CABLE_PLUGGED_AT_STATION = (
        PBComponentStateCode.COMPONENT_STATE_CODE_EV_CHARGING_CABLE_PLUGGED_AT_STATION
    )
    """The EV charging cable is plugged into the charging station."""

    EV_CHARGING_CABLE_PLUGGED_AT_EV = (
        PBComponentStateCode.COMPONENT_STATE_CODE_EV_CHARGING_CABLE_PLUGGED_AT_EV
    )
    """The EV charging cable is plugged into the vehicle."""

    EV_CHARGING_CABLE_LOCKED_AT_STATION = (
        PBComponentStateCode.COMPONENT_STATE_CODE_EV_CHARGING_CABLE_LOCKED_AT_STATION
    )
    """The EV charging cable is locked at the charging station end, indicating
    readiness for charging."""

    EV_CHARGING_CABLE_LOCKED_AT_EV = (
        PBComponentStateCode.COMPONENT_STATE_CODE_EV_CHARGING_CABLE_LOCKED_AT_EV
    )
    """The EV charging cable is locked at the vehicle end, indicating that charging is active."""

    RELAY_OPEN = PBComponentStateCode.COMPONENT_STATE_CODE_RELAY_OPEN
    """The relay is in an open state, meaning no current can flow through."""

    RELAY_CLOSED = PBComponentStateCode.COMPONENT_STATE_CODE_RELAY_CLOSED
    """The relay is in a closed state, allowing current to flow."""

    PRECHARGER_OPEN = PBComponentStateCode.COMPONENT_STATE_CODE_PRECHARGER_OPEN
    """The precharger circuit is open, meaning it's not currently active."""

    PRECHARGER_PRECHARGING = (
        PBComponentStateCode.COMPONENT_STATE_CODE_PRECHARGER_PRECHARGING
    )
    """The precharger is in a precharging state, preparing the main circuit for activation."""

    PRECHARGER_CLOSED = PBComponentStateCode.COMPONENT_STATE_CODE_PRECHARGER_CLOSED
    """The precharger circuit is closed, allowing full current to flow to the main circuit."""

    @classmethod
    def from_proto(
        cls, component_state: PBComponentStateCode.ValueType
    ) -> ComponentStateCode:
        """Convert a protobuf ComponentStateCode message to ComponentStateCode enum.

        Args:
            component_state: protobuf enum to convert

        Returns:
            Enum value corresponding to the protobuf message.
        """
        if not any(c.value == component_state for c in ComponentStateCode):
            return ComponentStateCode.UNSPECIFIED
        return cls(component_state)

    def to_proto(self) -> PBComponentStateCode.ValueType:
        """Convert a ComponentStateCode enum to protobuf ComponentStateCode message.

        Returns:
            Enum value corresponding to the protobuf message.
        """
        return self.value
