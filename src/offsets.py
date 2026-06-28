from __future__ import annotations
from dataclasses import dataclass, field
from typing import Dict

@dataclass
class OffsetData:
    GOD_MODE: int = 0x2a4b4d2
    UNLIMITED_AMMO: int = 0x2a4b519
    ESP_ENABLED: int = 0x2a4b66d
    SPEED_HACK: int = 0x2a4b6e0
    NO_RECOIL: int = 0x2a4b81e
    LOOT_UNLOCKER: int = 0x2a4b792
    BOUNTY_COMPLETE: int = 0x2a4b90b
    AIMBOT_FOV: int = 0x2a4b93c
    PLAYER_BASE: int = 0x1e8a3ca
    PLAYER_OFFSETS: list = field(default_factory=lambda: [0x0, 0x30, 0x8, 0x20])
    VERSION_OFFSETS: Dict[str, Dict[str,int]] = field(default_factory=lambda: {
        "2026.06.28-046": {
            "GOD_MODE": 0x2a4b4d2,
            "UNLIMITED_AMMO": 0x2a4b519,
        }
    })
    def get_for_version(self, ver): return self.VERSION_OFFSETS.get(ver, {})

offsets = OffsetData()
