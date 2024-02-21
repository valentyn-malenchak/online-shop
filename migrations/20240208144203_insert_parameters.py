"""Contains a migration that inserts/deletes parameters."""

import arrow
from mongodb_migrations.base import BaseMigration

from app.services.mongo.constants import MongoCollectionsEnum


class Migration(BaseMigration):  # type: ignore
    """Migration that inserts/deletes parameters."""

    def upgrade(self) -> None:
        """Inserts parameters."""
        self.db[MongoCollectionsEnum.PARAMETERS.value].insert_many(
            [
                {
                    "machine_name": "brand",
                    "name": "Brand",
                    "type": "STR",
                    "created_at": arrow.utcnow().datetime,
                    "updated_at": None,
                },
                {
                    "machine_name": "cpu",
                    "name": "CPU",
                    "type": "STR",
                    "created_at": arrow.utcnow().datetime,
                    "updated_at": None,
                },
                {
                    "machine_name": "cpu_cores_number",
                    "name": "CPU cores number",
                    "type": "INT",
                    "created_at": arrow.utcnow().datetime,
                    "updated_at": None,
                },
                {
                    "machine_name": "graphics_card",
                    "name": "Graphics card",
                    "type": "STR",
                    "created_at": arrow.utcnow().datetime,
                    "updated_at": None,
                },
                {
                    "machine_name": "graphics_card_type",
                    "name": "Graphics card type",
                    "type": "STR",
                    "created_at": arrow.utcnow().datetime,
                    "updated_at": None,
                },
                {
                    "machine_name": "vram",
                    "name": "Video RAM",
                    "type": "STR",
                    "created_at": arrow.utcnow().datetime,
                    "updated_at": None,
                },
                {
                    "machine_name": "motherboard_chipset",
                    "name": "Motherboard chipset",
                    "type": "STR",
                    "created_at": arrow.utcnow().datetime,
                    "updated_at": None,
                },
                {
                    "machine_name": "ram",
                    "name": "RAM",
                    "type": "STR",
                    "created_at": arrow.utcnow().datetime,
                    "updated_at": None,
                },
                {
                    "machine_name": "ram_slots",
                    "name": "RAM slots",
                    "type": "INT",
                    "created_at": arrow.utcnow().datetime,
                    "updated_at": None,
                },
                {
                    "machine_name": "ram_type",
                    "name": "RAM type",
                    "type": "STR",
                    "created_at": arrow.utcnow().datetime,
                    "updated_at": None,
                },
                {
                    "machine_name": "hdd",
                    "name": "HDD",
                    "type": "STR",
                    "created_at": arrow.utcnow().datetime,
                    "updated_at": None,
                },
                {
                    "machine_name": "hdd_space",
                    "name": "HDD space",
                    "type": "STR",
                    "created_at": arrow.utcnow().datetime,
                    "updated_at": None,
                },
                {
                    "machine_name": "ssd",
                    "name": "SSD",
                    "type": "STR",
                    "created_at": arrow.utcnow().datetime,
                    "updated_at": None,
                },
                {
                    "machine_name": "ssd_space",
                    "name": "SSD space",
                    "type": "STR",
                    "created_at": arrow.utcnow().datetime,
                    "updated_at": None,
                },
                {
                    "machine_name": "monitor",
                    "name": "Monitor",
                    "type": "STR",
                    "created_at": arrow.utcnow().datetime,
                    "updated_at": None,
                },
                {
                    "machine_name": "monitor_screen_size",
                    "name": "Monitor screen size",
                    "type": "STR",
                    "created_at": arrow.utcnow().datetime,
                    "updated_at": None,
                },
                {
                    "machine_name": "class",
                    "name": "Class",
                    "type": "LIST",
                    "created_at": arrow.utcnow().datetime,
                    "updated_at": None,
                },
                {
                    "machine_name": "has_wifi",
                    "name": "Wifi",
                    "type": "BOOL",
                    "created_at": arrow.utcnow().datetime,
                    "updated_at": None,
                },
                {
                    "machine_name": "has_bluetooth",
                    "name": "Bluetooth",
                    "type": "BOOL",
                    "created_at": arrow.utcnow().datetime,
                    "updated_at": None,
                },
                {
                    "machine_name": "no_wireless_connection",
                    "name": "No wireless connection",
                    "type": "BOOL",
                    "created_at": arrow.utcnow().datetime,
                    "updated_at": None,
                },
                {
                    "machine_name": "os",
                    "name": "Operation system",
                    "type": "STR",
                    "created_at": arrow.utcnow().datetime,
                    "updated_at": None,
                },
                {
                    "machine_name": "year",
                    "name": "Manufacture year",
                    "type": "INT",
                    "created_at": arrow.utcnow().datetime,
                    "updated_at": None,
                },
                {
                    "machine_name": "warranty",
                    "name": "Warranty",
                    "type": "STR",
                    "created_at": arrow.utcnow().datetime,
                    "updated_at": None,
                },
                {
                    "machine_name": "country_of_production",
                    "name": "County of production",
                    "type": "STR",
                    "created_at": arrow.utcnow().datetime,
                    "updated_at": None,
                },
                {
                    "machine_name": "screen_type",
                    "name": "Screen type",
                    "type": "STR",
                    "created_at": arrow.utcnow().datetime,
                    "updated_at": None,
                },
                {
                    "machine_name": "screen_resolution",
                    "name": "Screen resolution",
                    "type": "STR",
                    "created_at": arrow.utcnow().datetime,
                    "updated_at": None,
                },
                {
                    "machine_name": "screen_refresh_rate",
                    "name": "Screen refresh rate",
                    "type": "STR",
                    "created_at": arrow.utcnow().datetime,
                    "updated_at": None,
                },
                {
                    "machine_name": "screen_ratio",
                    "name": "Screen ratio",
                    "type": "STR",
                    "created_at": arrow.utcnow().datetime,
                    "updated_at": None,
                },
                {
                    "machine_name": "screen_size",
                    "name": "Screen size",
                    "type": "STR",
                    "created_at": arrow.utcnow().datetime,
                    "updated_at": None,
                },
                {
                    "machine_name": "battery_capacity",
                    "name": "Battery capacity",
                    "type": "STR",
                    "created_at": arrow.utcnow().datetime,
                    "updated_at": None,
                },
                {
                    "machine_name": "has_fingerprint_identification",
                    "name": "Fingerprint identification",
                    "type": "BOOL",
                    "created_at": arrow.utcnow().datetime,
                    "updated_at": None,
                },
                {
                    "machine_name": "has_keyboard_backlight",
                    "name": "Keyboard backlight",
                    "type": "BOOL",
                    "created_at": arrow.utcnow().datetime,
                    "updated_at": None,
                },
                {
                    "machine_name": "has_touch_screen",
                    "name": "Touch screen",
                    "type": "BOOL",
                    "created_at": arrow.utcnow().datetime,
                    "updated_at": None,
                },
                {
                    "machine_name": "color",
                    "name": "Color",
                    "type": "STR",
                    "created_at": arrow.utcnow().datetime,
                    "updated_at": None,
                },
                {
                    "machine_name": "has_smarttv",
                    "name": "SmartTV",
                    "type": "BOOL",
                    "created_at": arrow.utcnow().datetime,
                    "updated_at": None,
                },
                {
                    "machine_name": "platform",
                    "name": "SmartTV",
                    "type": "STR",
                    "created_at": arrow.utcnow().datetime,
                    "updated_at": None,
                },
                {
                    "machine_name": "tv_tuner",
                    "name": "TV tuner",
                    "type": "LIST",
                    "created_at": arrow.utcnow().datetime,
                    "updated_at": None,
                },
                {
                    "machine_name": "supports_3d",
                    "name": "3D",
                    "type": "BOOL",
                    "created_at": arrow.utcnow().datetime,
                    "updated_at": None,
                },
                {
                    "machine_name": "supports_hdr",
                    "name": "HDR",
                    "type": "BOOL",
                    "created_at": arrow.utcnow().datetime,
                    "updated_at": None,
                },
                {
                    "machine_name": "supports_vrr",
                    "name": "VRR",
                    "type": "BOOL",
                    "created_at": arrow.utcnow().datetime,
                    "updated_at": None,
                },
                {
                    "machine_name": "sound_output_power",
                    "name": "Sound output power",
                    "type": "STR",
                    "created_at": arrow.utcnow().datetime,
                    "updated_at": None,
                },
                {
                    "machine_name": "built_in_memory",
                    "name": "Built-in memory",
                    "type": "STR",
                    "created_at": arrow.utcnow().datetime,
                    "updated_at": None,
                },
                {
                    "machine_name": "has_nfc",
                    "name": "NFC",
                    "type": "BOOL",
                    "created_at": arrow.utcnow().datetime,
                    "updated_at": None,
                },
                {
                    "machine_name": "has_infrared_port",
                    "name": "Infrared port",
                    "type": "BOOL",
                    "created_at": arrow.utcnow().datetime,
                    "updated_at": None,
                },
                {
                    "machine_name": "supports_wireless_charging",
                    "name": "Wireless charging",
                    "type": "BOOL",
                    "created_at": arrow.utcnow().datetime,
                    "updated_at": None,
                },
                {
                    "machine_name": "has_micro_jack",
                    "name": "Micro-Jack",
                    "type": "BOOL",
                    "created_at": arrow.utcnow().datetime,
                    "updated_at": None,
                },
                {
                    "machine_name": "has_mini_jack",
                    "name": "Mini-Jack",
                    "type": "BOOL",
                    "created_at": arrow.utcnow().datetime,
                    "updated_at": None,
                },
                {
                    "machine_name": "has_apple_lightning",
                    "name": "Apple Lightning",
                    "type": "BOOL",
                    "created_at": arrow.utcnow().datetime,
                    "updated_at": None,
                },
                {
                    "machine_name": "has_usb_type_c",
                    "name": "USB Type-C",
                    "type": "BOOL",
                    "created_at": arrow.utcnow().datetime,
                    "updated_at": None,
                },
                {
                    "machine_name": "main_camera_resolution",
                    "name": "Main camera resolution",
                    "type": "STR",
                    "created_at": arrow.utcnow().datetime,
                    "updated_at": None,
                },
                {
                    "machine_name": "front_camera_resolution",
                    "name": "Front camera resolution",
                    "type": "STR",
                    "created_at": arrow.utcnow().datetime,
                    "updated_at": None,
                },
                {
                    "machine_name": "sim_cards_number",
                    "name": "SIM-cards number",
                    "type": "INT",
                    "created_at": arrow.utcnow().datetime,
                    "updated_at": None,
                },
                {
                    "machine_name": "body_material",
                    "name": "Body material",
                    "type": "STR",
                    "created_at": arrow.utcnow().datetime,
                    "updated_at": None,
                },
                {
                    "machine_name": "model",
                    "name": "Model",
                    "type": "STR",
                    "created_at": arrow.utcnow().datetime,
                    "updated_at": None,
                },
                {
                    "machine_name": "complete_set",
                    "name": "Complete set",
                    "type": "STR",
                    "created_at": arrow.utcnow().datetime,
                    "updated_at": None,
                },
                {
                    "machine_name": "game_console",
                    "name": "Game console",
                    "type": "STR",
                    "created_at": arrow.utcnow().datetime,
                    "updated_at": None,
                },
                {
                    "machine_name": "has_disk_drive",
                    "name": "Disk drive",
                    "type": "BOOL",
                    "created_at": arrow.utcnow().datetime,
                    "updated_at": None,
                },
                {
                    "machine_name": "supports_vr",
                    "name": "VR",
                    "type": "BOOL",
                    "created_at": arrow.utcnow().datetime,
                    "updated_at": None,
                },
                {
                    "machine_name": "control_tool",
                    "name": "Control tool",
                    "type": "STR",
                    "created_at": arrow.utcnow().datetime,
                    "updated_at": None,
                },
                {
                    "machine_name": "maximum_supported_resolution",
                    "name": "Maximum supported resolution",
                    "type": "STR",
                    "created_at": arrow.utcnow().datetime,
                    "updated_at": None,
                },
                {
                    "machine_name": "type",
                    "name": "Type",
                    "type": "STR",
                    "created_at": arrow.utcnow().datetime,
                    "updated_at": None,
                },
                {
                    "machine_name": "family",
                    "name": "Family",
                    "type": "STR",
                    "created_at": arrow.utcnow().datetime,
                    "updated_at": None,
                },
                {
                    "machine_name": "socket",
                    "name": "Socket",
                    "type": "STR",
                    "created_at": arrow.utcnow().datetime,
                    "updated_at": None,
                },
                {
                    "machine_name": "cpu_threads_number",
                    "name": "CPU threads number",
                    "type": "STR",
                    "created_at": arrow.utcnow().datetime,
                    "updated_at": None,
                },
                {
                    "machine_name": "base_clock_frequency",
                    "name": "Base clock frequency",
                    "type": "STR",
                    "created_at": arrow.utcnow().datetime,
                    "updated_at": None,
                },
                {
                    "machine_name": "maximum_clock_frequency",
                    "name": "Maximum clock frequency",
                    "type": "STR",
                    "created_at": arrow.utcnow().datetime,
                    "updated_at": None,
                },
                {
                    "machine_name": "intel_generation",
                    "name": "Intel generation",
                    "type": "STR",
                    "created_at": arrow.utcnow().datetime,
                    "updated_at": None,
                },
                {
                    "machine_name": "amd_generation",
                    "name": "AMD generation",
                    "type": "STR",
                    "created_at": arrow.utcnow().datetime,
                    "updated_at": None,
                },
                {
                    "machine_name": "supports_integrated_graphics",
                    "name": "Integrated graphics",
                    "type": "BOOL",
                    "created_at": arrow.utcnow().datetime,
                    "updated_at": None,
                },
                {
                    "machine_name": "storage",
                    "name": "Storage",
                    "type": "STR",
                    "created_at": arrow.utcnow().datetime,
                    "updated_at": None,
                },
                {
                    "machine_name": "connection_interface",
                    "name": "Connection interface",
                    "type": "LIST",
                    "created_at": arrow.utcnow().datetime,
                    "updated_at": None,
                },
                {
                    "machine_name": "form_factor",
                    "name": "Form factor",
                    "type": "STR",
                    "created_at": arrow.utcnow().datetime,
                    "updated_at": None,
                },
                {
                    "machine_name": "purpose",
                    "name": "Purpose",
                    "type": "LIST",
                    "created_at": arrow.utcnow().datetime,
                    "updated_at": None,
                },
                {
                    "machine_name": "spindle_rotation_speed",
                    "name": "Spindle rotation speed",
                    "type": "STR",
                    "created_at": arrow.utcnow().datetime,
                    "updated_at": None,
                },
                {
                    "machine_name": "technology",
                    "name": "Technology",
                    "type": "STR",
                    "created_at": arrow.utcnow().datetime,
                    "updated_at": None,
                },
                {
                    "machine_name": "type_of_memory_elements",
                    "name": "Type of memory elements",
                    "type": "STR",
                    "created_at": arrow.utcnow().datetime,
                    "updated_at": None,
                },
                {
                    "machine_name": "memory",
                    "name": "Memory",
                    "type": "STR",
                    "created_at": arrow.utcnow().datetime,
                    "updated_at": None,
                },
                {
                    "machine_name": "memory_frequency",
                    "name": "Memory frequency",
                    "type": "STR",
                    "created_at": arrow.utcnow().datetime,
                    "updated_at": None,
                },
                {
                    "machine_name": "memory_type",
                    "name": "Memory type",
                    "type": "STR",
                    "created_at": arrow.utcnow().datetime,
                    "updated_at": None,
                },
                {
                    "machine_name": "bar_numbers",
                    "name": "Bars number",
                    "type": "INT",
                    "created_at": arrow.utcnow().datetime,
                    "updated_at": None,
                },
                {
                    "machine_name": "cas_latency",
                    "name": "CAS latency",
                    "type": "STR",
                    "created_at": arrow.utcnow().datetime,
                    "updated_at": None,
                },
                {
                    "machine_name": "graphic_chip",
                    "name": "Graphic chip",
                    "type": "STR",
                    "created_at": arrow.utcnow().datetime,
                    "updated_at": None,
                },
                {
                    "machine_name": "memory_bus_bit_size",
                    "name": "Memory bus bit size",
                    "type": "STR",
                    "created_at": arrow.utcnow().datetime,
                    "updated_at": None,
                },
                {
                    "machine_name": "additional_power",
                    "name": "Additional power",
                    "type": "STR",
                    "created_at": arrow.utcnow().datetime,
                    "updated_at": None,
                },
                {
                    "machine_name": "cooling_system_type",
                    "name": "Cooling system type",
                    "type": "STR",
                    "created_at": arrow.utcnow().datetime,
                    "updated_at": None,
                },
                {
                    "machine_name": "power",
                    "name": "Power",
                    "type": "STR",
                    "created_at": arrow.utcnow().datetime,
                    "updated_at": None,
                },
                {
                    "machine_name": "supports_80_plus",
                    "name": "80 PLUS",
                    "type": "BOOL",
                    "created_at": arrow.utcnow().datetime,
                    "updated_at": None,
                },
                {
                    "machine_name": "connector",
                    "name": "Connector",
                    "type": "STR",
                    "created_at": arrow.utcnow().datetime,
                    "updated_at": None,
                },
                {
                    "machine_name": "protection_technologies",
                    "name": "Protection technologies",
                    "type": "LIST",
                    "created_at": arrow.utcnow().datetime,
                    "updated_at": None,
                },
                {
                    "machine_name": "motherboard_power_supply",
                    "name": "Motherboard power supply",
                    "type": "STR",
                    "created_at": arrow.utcnow().datetime,
                    "updated_at": None,
                },
                {
                    "machine_name": "voltage",
                    "name": "Voltage",
                    "type": "STR",
                    "created_at": arrow.utcnow().datetime,
                    "updated_at": None,
                },
                {
                    "machine_name": (
                        "number_of_additional_power_connectors_for_video_cards"
                    ),
                    "name": "Number of additional power connectors for video cards",
                    "type": "INT",
                    "created_at": arrow.utcnow().datetime,
                    "updated_at": None,
                },
                {
                    "machine_name": "sata_connections_number",
                    "name": "SATA connections number",
                    "type": "INT",
                    "created_at": arrow.utcnow().datetime,
                    "updated_at": None,
                },
                {
                    "machine_name": "memory_types_support",
                    "name": "Memory types support",
                    "type": "LIST",
                    "created_at": arrow.utcnow().datetime,
                    "updated_at": None,
                },
                {
                    "machine_name": "wireless_interface",
                    "name": "Wireless interface",
                    "type": "LIST",
                    "created_at": arrow.utcnow().datetime,
                    "updated_at": None,
                },
                {
                    "machine_name": "m2_connectors_number",
                    "name": "M.2 (NGFF) connectors number",
                    "type": "INT",
                    "created_at": arrow.utcnow().datetime,
                    "updated_at": None,
                },
                {
                    "machine_name": "maximum_memory_frequency",
                    "name": "Maximum memory frequency",
                    "type": "STR",
                    "created_at": arrow.utcnow().datetime,
                    "updated_at": None,
                },
                {
                    "machine_name": "video_outputs",
                    "name": "Video outputs",
                    "type": "LIST",
                    "created_at": arrow.utcnow().datetime,
                    "updated_at": None,
                },
                {
                    "machine_name": "pci_express_x16",
                    "name": "PCI Express x16",
                    "type": "INT",
                    "created_at": arrow.utcnow().datetime,
                    "updated_at": None,
                },
                {
                    "machine_name": "pci_express_x8",
                    "name": "PCI Express x8",
                    "type": "INT",
                    "created_at": arrow.utcnow().datetime,
                    "updated_at": None,
                },
                {
                    "machine_name": "pci_express_x4",
                    "name": "PCI Express x4",
                    "type": "INT",
                    "created_at": arrow.utcnow().datetime,
                    "updated_at": None,
                },
                {
                    "machine_name": "pci_express_x1",
                    "name": "PCI Express x1",
                    "type": "INT",
                    "created_at": arrow.utcnow().datetime,
                    "updated_at": None,
                },
                {
                    "machine_name": "pci",
                    "name": "PCI",
                    "type": "INT",
                    "created_at": arrow.utcnow().datetime,
                    "updated_at": None,
                },
                {
                    "machine_name": "network_interface",
                    "name": "Network interface",
                    "type": "STR",
                    "created_at": arrow.utcnow().datetime,
                    "updated_at": None,
                },
                {
                    "machine_name": "usb",
                    "name": "USB",
                    "type": "LIST",
                    "created_at": arrow.utcnow().datetime,
                    "updated_at": None,
                },
                {
                    "machine_name": "digital_audio_jack",
                    "name": "Digital audio jack",
                    "type": "LIST",
                    "created_at": arrow.utcnow().datetime,
                    "updated_at": None,
                },
                {
                    "machine_name": "maximum_supported_tdp_value",
                    "name": "Maximum supported TDP value",
                    "type": "STR",
                    "created_at": arrow.utcnow().datetime,
                    "updated_at": None,
                },
                {
                    "machine_name": "u2_connector",
                    "name": "U.2 connector",
                    "type": "INT",
                    "created_at": arrow.utcnow().datetime,
                    "updated_at": None,
                },
                {
                    "machine_name": "satae",
                    "name": "SATAe",
                    "type": "INT",
                    "created_at": arrow.utcnow().datetime,
                    "updated_at": None,
                },
                {
                    "machine_name": "msata",
                    "name": "mSATA",
                    "type": "INT",
                    "created_at": arrow.utcnow().datetime,
                    "updated_at": None,
                },
                {
                    "machine_name": "motherboard_form_factor",
                    "name": "Motherboard form factor",
                    "type": "STR",
                    "created_at": arrow.utcnow().datetime,
                    "updated_at": None,
                },
                {
                    "machine_name": "power_of_the_power_supply",
                    "name": "Power of the power supply",
                    "type": "STR",
                    "created_at": arrow.utcnow().datetime,
                    "updated_at": None,
                },
                {
                    "machine_name": "installed_fans_number",
                    "name": "Installed fans number",
                    "type": "INT",
                    "created_at": arrow.utcnow().datetime,
                    "updated_at": None,
                },
                {
                    "machine_name": "body_type",
                    "name": "Body type",
                    "type": "STR",
                    "created_at": arrow.utcnow().datetime,
                    "updated_at": None,
                },
                {
                    "machine_name": "front_panel_connectors",
                    "name": "Front panel connectors",
                    "type": "LIST",
                    "created_at": arrow.utcnow().datetime,
                    "updated_at": None,
                },
                {
                    "machine_name": "view",
                    "name": "View",
                    "type": "STR",
                    "created_at": arrow.utcnow().datetime,
                    "updated_at": None,
                },
                {
                    "machine_name": "fan_size",
                    "name": "Fan size",
                    "type": "STR",
                    "created_at": arrow.utcnow().datetime,
                    "updated_at": None,
                },
                {
                    "machine_name": "maximum_tdp",
                    "name": "Maximum TDP",
                    "type": "STR",
                    "created_at": arrow.utcnow().datetime,
                    "updated_at": None,
                },
                {
                    "machine_name": "power_supply_connector",
                    "name": "Power supply connector",
                    "type": "STR",
                    "created_at": arrow.utcnow().datetime,
                    "updated_at": None,
                },
                {
                    "machine_name": "bearing_type",
                    "name": "Bering type",
                    "type": "STR",
                    "created_at": arrow.utcnow().datetime,
                    "updated_at": None,
                },
                {
                    "machine_name": "connection_type",
                    "name": "Connection type",
                    "type": "STR",
                    "created_at": arrow.utcnow().datetime,
                    "updated_at": None,
                },
                {
                    "machine_name": "form",
                    "name": "Form",
                    "type": "STR",
                    "created_at": arrow.utcnow().datetime,
                    "updated_at": None,
                },
                {
                    "machine_name": "size",
                    "name": "Size",
                    "type": "STR",
                    "created_at": arrow.utcnow().datetime,
                    "updated_at": None,
                },
                {
                    "machine_name": "buttons_number",
                    "name": "Buttons number",
                    "type": "INT",
                    "created_at": arrow.utcnow().datetime,
                    "updated_at": None,
                },
                {
                    "machine_name": "maximum_sensor_resolution",
                    "name": "Maximum sensor resolution (dpi)",
                    "type": "INT",
                    "created_at": arrow.utcnow().datetime,
                    "updated_at": None,
                },
            ]
        )

    def downgrade(self) -> None:
        """Drops parameters."""
        self.db[MongoCollectionsEnum.PARAMETERS.value].delete_many(filter={})
