from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable


@dataclass(frozen=True, slots=True)
class CustomEmoji:
    name: str
    id: int
    animated: bool = False

    @property
    def mention(self) -> str:
        prefix = "a" if self.animated else ""
        return f"<{prefix}:{self.name}:{self.id}>"

    @property
    def cdn_url(self) -> str:
        extension = "gif" if self.animated else "png"
        return f"https://cdn.discordapp.com/emojis/{self.id}.{extension}"

    def __str__(self) -> str:
        return self.mention


# Emoji constants
EMOJI_37496ALERT = CustomEmoji("rem_alert", 1525739908826660984)
EMOJI_7CLUB_BAN = CustomEmoji("rem_ban", 1525739944205746286)
ROSE = CustomEmoji("rem_rose", 1525740415326621746)
AUTOREACT = CustomEmoji("rem_autoreact", 1525739929978798202)
AUTOROLE = CustomEmoji("rem_autorole", 1525739936966381638)
REM_OWNER = CustomEmoji("rem_owner", 1525740365976440902)
BLUEDOT = CustomEmoji("rem_dot", 1525740064988991689)
BOTS = CustomEmoji("rem_bots", 1525739964845785089)
BROWSER = CustomEmoji("rem_browser", 1525739972294873268)
COMMANDS = CustomEmoji("rem_commands", 1525739993362993163)
CROSSICON = CustomEmoji("rem_cross", 1525740000728191106)
CUSTOMROLE = CustomEmoji("rem_customrole", 1525740021758296104)
DC_REDCROWNESPORTS = CustomEmoji("rem_crown", 1525740014703476877)
DELETE = CustomEmoji("rem_delete", 1525740028779692143)
DENIED = CustomEmoji("rem_denied", 1525740035838578873)
DISABLED1 = CustomEmoji("rem_disabled", 1525740050313248828)
DND = CustomEmoji("rem_dnd", 1525740057758269521)
ENABLED = CustomEmoji("rem_enabled", 1525740079040041141)
ENABLED_160063 = CustomEmoji("rem_on", 1525740351527059529)
EXTRA = CustomEmoji("rem_extra", 1525740085977415710)
FILDER = CustomEmoji("rem_folder", 1525740099978133604)
FILE = CustomEmoji("rem_file", 1525740092990423071)
FORWARD = CustomEmoji("rem_forward", 1525740107070574622)
GAMES = CustomEmoji("rem_games", 1525740121448644648)
GEAR = CustomEmoji("rem_settings", 1525740429096648948)
GIFD = CustomEmoji("rem_gif_off", 1525740128365183239)
GIFN = CustomEmoji("rem_gif_on", 1525740135386316952)
GIVEAWAY = CustomEmoji("rem_giveaway", 1525740142730412173)
GIVEAWAY_644980 = GIVEAWAY
GIVEAWAYS = CustomEmoji("rem_giveaways", 1525740149785231431)
GREET = CustomEmoji("rem_welcome", 1525740608025788416)
HEADMOD = CustomEmoji("rem_headmod", 1525740156777271507)
HEART_EM = CustomEmoji("rem_heart", 1525740163861577858)
HEERIYE = CustomEmoji("rem_note", 1525740327925846177)
HOME = CustomEmoji("rem_home", 1525740185210327060)
ICON_BOOSTER = CustomEmoji("rem_booster", 1525739951252045884)
ICON_PING = CustomEmoji("rem_ping", 1525740387027652658)
ICONARROWRIGHT = CustomEmoji("rem_arrow_right", 1525739922860802130)
ICONLOAD = CustomEmoji("rem_load", 1525740235336450118)
ICONS_BOT = CustomEmoji("rem_bot", 1525739958155874324)
ICONS_CHANNEL = CustomEmoji("rem_channel", 1525739978934452287)
ICONS_DISCORDBOTDEV = CustomEmoji("rem_dev", 1525740043300376746)
ICONS_MUSIC = CustomEmoji("rem_music_note", 1525740306484428884)
ICONS_NEXT = CustomEmoji("rem_next", 1525740313841238197)
ICONS_PAUSE = CustomEmoji("rem_pause", 1525740372569882686)
ICONS_PLUS = CustomEmoji("rem_plus", 1525740394166616094)
ICONS_WARNING = CustomEmoji("rem_warning_sm", 1525740600924704919)
ICONSETTING = CustomEmoji("rem_cog", 1525739986505306162)
IDLE = CustomEmoji("rem_idle", 1525740192273662123)
IGNORE = CustomEmoji("rem_ignore", 1525740199517225070)
INFO = CustomEmoji("rem_info", 1525740206685163610)
INVITETRACKER = CustomEmoji("rem_invites", 1525740213404438602)
JIOSAAVN = CustomEmoji("rem_jiosaavn", 1525740220983541791)
KING = CustomEmoji("rem_king", 1525740228235628605)
LAND_YILDIZ = CustomEmoji("rem_star", 1525740472700637346)
LAND_YILDIZ_722475 = LAND_YILDIZ
LOADING = CustomEmoji("rem_loading", 1525740242538332263)
LOADING_461233 = LOADING
LOGGING = CustomEmoji("rem_logging", 1525740249534300210)
MAX__A = CustomEmoji("rem_volume", 1525740579827224727)
MENTION = CustomEmoji("rem_mention", 1525740256157110274)
ML_CROSS = CustomEmoji("rem_cross_ml", 1525740007640404048)
MOBILE = CustomEmoji("rem_mobile", 1525740263455064114)
MOD = CustomEmoji("rem_mod", 1525740270216282194)
MODERATION = CustomEmoji("rem_moderation", 1525740284879700018)
MODULE = CustomEmoji("rem_module", 1525740291993370684)
MUSIC = CustomEmoji("rem_music", 1525740299379540019)
MUSIC_116319 = MUSIC
MUSICSTOP_ICONS = CustomEmoji("rem_stop", 1525740493617631233)
NEXT = CustomEmoji("rem_skip_fwd", 1525740451120812052)
OFFLINE = CustomEmoji("rem_offline", 1525740341972570214)
REM_NO = CustomEmoji("rem_no", 1525740320925679636)
REM_NOTIFY = CustomEmoji("rem_notify", 1525740334976467066)
REM_STAFF = CustomEmoji("rem_staff", 1525740465574514930)
REM_SUCCESS = CustomEmoji("rem_success", 1525740500999602227)
REM_ARROW = CustomEmoji("rem_arrow", 1525739915503993033)
ONLINE = CustomEmoji("rem_online", 1525740358946783364)
PC = CustomEmoji("rem_pc", 1525740380014907422)
PREMIUM = CustomEmoji("rem_premium", 1525740400877371425)
QUESTIONS = CustomEmoji("rem_help", 1525740177820090428)
RED_DOT = CustomEmoji("rem_dot_red", 1525740072043941908)
REDHEART = CustomEmoji("rem_heart_red", 1525740170572464240)
REWIND1 = CustomEmoji("rem_rewind", 1525740407835721760)
RIVERSE_FUN = CustomEmoji("rem_fun", 1525740114096034013)
SECURITY = CustomEmoji("rem_security", 1525740422121521407)
SG_RD = CustomEmoji("rem_status_dot", 1525740486801752296)
SHUFFLE = CustomEmoji("rem_shuffle", 1525740436646268939)
SKIP = CustomEmoji("rem_skip", 1525740443592167578)
SOUNDCLOUD = CustomEmoji("rem_soundcloud", 1525740458355986545)
SQ_HEADMOD = CustomEmoji("rem_mod_shield", 1525740277854240798)
STAR = CustomEmoji("rem_star_badge", 1525740479986008077)
STAR_147803 = STAR
TICK = CustomEmoji("rem_tick", 1525740508222066829)
TICK_RED = CustomEmoji("rem_tick_red", 1525740515281080441)
TICKET = CustomEmoji("rem_ticket", 1525740529524936775)
TIMER = CustomEmoji("rem_timer", 1525740537381126185)
U_ADMIN = CustomEmoji("rem_admin", 1525739901587292172)
UPTIME = CustomEmoji("rem_uptime", 1525740544645533846)
USER = CustomEmoji("rem_user", 1525740551716999170)
UTILITY = CustomEmoji("rem_utility", 1525740558503379035)
VANITYROLES = CustomEmoji("rem_vanity", 1525740565776306306)
VOICE = CustomEmoji("rem_voice", 1525740572734914714)
VOICE_003466 = VOICE
WARNING = CustomEmoji("rem_warning", 1525740586819125420)
WARNINGICON = CustomEmoji("rem_warning_badge", 1525740593953771703)
YOUTUBE = CustomEmoji("rem_youtube", 1525740615013236834)
YOUTUBE_570841 = YOUTUBE
ZTICK = CustomEmoji("rem_tick_round", 1525740522369712350)


def _constant_emojis() -> dict[str, CustomEmoji]:
    return {
        name: value
        for name, value in globals().items()
        if name.isupper() and isinstance(value, CustomEmoji)
    }


def _rebuild_indexes() -> None:
    EMOJIS.clear()
    EMOJIS_BY_ID.clear()

    for emoji in _constant_emojis().values():
        EMOJIS[emoji.name] = emoji
        EMOJIS_BY_ID[emoji.id] = emoji


EMOJIS: dict[str, CustomEmoji] = {}
EMOJIS_BY_ID: dict[int, CustomEmoji] = {}


def get(name: str) -> CustomEmoji:
    return EMOJIS[name]


def get_by_id(emoji_id: int) -> CustomEmoji:
    return EMOJIS_BY_ID[emoji_id]


def mention(name: str) -> str:
    return get(name).mention


def all_custom_emojis() -> tuple[CustomEmoji, ...]:
    return tuple(EMOJIS_BY_ID.values())


def apply_application_emojis(application_emojis: Iterable[object]) -> int:
    by_name = {
        str(getattr(emoji, "name")).lower(): emoji
        for emoji in application_emojis
        if getattr(emoji, "name", None) and getattr(emoji, "id", None)
    }

    updates = 0

    for constant_name, current in _constant_emojis().items():
        application_emoji = by_name.get(current.name.lower())
        if application_emoji is None:
            continue

        next_emoji = CustomEmoji(
            name=str(getattr(application_emoji, "name")),
            id=int(getattr(application_emoji, "id")),
            animated=bool(getattr(application_emoji, "animated", False)),
        )

        if next_emoji != current:
            globals()[constant_name] = next_emoji
            updates += 1

    if updates:
        _rebuild_indexes()

    return updates


_rebuild_indexes()
