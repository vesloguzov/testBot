#!/usr/bin/env python
import requests
import random
import telebot
import pickle
from telebot import types
from telebot.types import Message
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

# f = open(r'users.pkl', 'rb')
# print(f)
# try:
#     users = pickle.load(f)
# except:
#     users = set()
# f.close()

# r = requests.get(f'https://api.telegram.org/{}/getUpdates')

stickers = ["CAADAgADBgUAAnwFBxsXXw32UH5NowI",
"CAADAgADDAUAAnwFBxtJTBGghWawtAI",
"CAADBAADBAEAAmuuXglkrEWPVloqrQI",
"CAADBAADGwEAAmuuXglEoAToyWLmiQI",
"CAADBAADIAEAAmuuXgkJ-8kbj90p1AI",
"CAADBAADJQEAAmuuXgm3cQUo-y8R_wI",
"CAADBAADNwEAAmuuXglK7X34F2rmlQI",
"CAADBAADOgEAAmuuXgmasYVZ3o9jeQI",
"CAADBAADPAEAAmuuXgllNsVC9rDlEAI",
"CAADBAADQAEAAmuuXgm0Qsx9DNuN4QI",
"CAADBAADVgEAAmuuXgkpPDFsnPiu2wI",
"CAADBAADYAEAAmuuXgldxtDpzTv4lQI",
"CAADBAADYAEAAmuuXgldxtDpzTv4lQI",
"CAADAgADpAADNmLjBbuFIoqViIS6Ag",
"CAADAgAD1AADNmLjBUIbc1h206SuAg",
"CAADAgAD2gADNmLjBf5sPUXicvkmAg",
"CAADAgADCgEAAjZi4wVjHLC_sG5GoQI",
"CAADAgADFgEAAjZi4wWMpfR1KQ96gAI",
"CAADAgADEgEAAjZi4wWkbBDGnLIt5AI",
"CAADAgAD3AADV08VCG005EUio8c0Ag",
"CAADAgADnwADV08VCMRycuQqC77iAg",
"CAADAgADpQADV08VCCDlTCVmMlOuAg",
"CAADAgADtQADV08VCMl7ixqqpI_lAg",
"CAADAgADuAADV08VCIU2WpK6h9FGAg",
"CAADAgAD3QADV08VCB8ZwhZqY2gWAg",
"CAADAgAD7QADV08VCL-HAAH5QxBkxQI",
"CAADAgAD3wADV08VCGrlTPAr12swAg",
"CAADAgAD_wIAAkcVaAlf4TWmtoGfKgI",
"CAADAgAD6gIAAkcVaAn4-KMKZ_78IgI",
"CAADAgADAQMAAkcVaAm8k2nQpB1EVAI",
"CAADAgAEAwACRxVoCfVBcIGLa635Ag",
"CAADAgAD7QIAAkcVaAkBNYH8EbhGPAI",
"CAADAgAD4QIAAkcVaAkD54WNQEaR5wI",
"CAADAgAD3gADN20QAjBqNmIyb7S2Ag",
"CAADAgAD7gADN20QAk_PWqmcpfQeAg",
"CAADAgADKgEAAjdtEAIXLp6mv2VZvAI",
"CAADAgADNgEAAjdtEAL9LG4WNA0r7AI",
"CAADAgADOgEAAjdtEALfH3MIHx3lNQI",
"CAADAgADvAEAAjdtEALhUhIwMog32wI",
"CAADAgADLQADS9C7EDHq8s4rVeHVAg",
"CAADAgADMwADS9C7EDZPrpjdIh-4Ag",
"CAADAgADSQADS9C7EHE2zbU49o-cAg",
"CAADAgADTAADS9C7EKcLcpzQCmyKAg",
"CAADAgADVAADS9C7EFTrxLbIO2ufAg",
"CAADAgADFQADd0tuHd1miIDiJ2mlAg",
"CAADAgADIAoAAm4y2AABM9mfsniANPQC",
"CAADAgADMAADd0tuHbAFCRr408X0Ag",
"CAADAgADQQoAAm4y2AAB91ExzjLMrlgC",
"CAADAgADTQoAAm4y2AABca3m-C95Yq4C",
"CAADAgADLgoAAm4y2AABdlggYmqzq3QC",
"CAADAgADUAAD6u8-Cu7iG1RZyxbYAg",
"CAADAgADVgAD6u8-Chpv0T03i99ZAg",
"CAADAgADWAAD6u8-Cifg_alo0rbnAg",
"CAADAgADVwAD6u8-CmqeaRQ0d06pAg",
"CAADAgADNAADrJzIDxoJydSMkeGqAg",
"CAADAgADAQADd0tuHVgO5N1b1pu1Ag",
"CAADAgADNAADrJzIDxoJydSMkeGqAg",
"CAADAgADAgADd0tuHZpiyinvlv3hAg",
"CAADAgADIwADrJzID7dUim6f3scWAg",
"CAADAgADAwADd0tuHXA8rvnwrS2cAg",
"CAADAgADMgADrJzID32VfG7KOh-fAg",
"CAADAgADIgADrJzIDzceY793toABAg",
"CAADAgADOAADrJzID4L1EmHL_dMLAg",
"CAADAgADBAADd0tuHayOT2P6XHR3Ag",
"CAADAgADPAADrJzIDyDwlbX2IWUvAg",
"CAADAgADPQkAAtA90ghjP37h1mmudwI",
"CAADAgADCAADd0tuHWVY1erMaepbAg",
"CAADAgADRwkAAtA90gg4eadIePe3cQI",
"CAADAgADSwkAAtA90gh-epXm4mLvOwI",
"CAADAgADRgkAAtA90gje3ocWitYvUgI",
"CAADAgADWAkAAtA90gjfZygZwJZxNAI",
"CAADAgADYgkAAtA90gjrC3-JmHH1aAI",
"CAADAgADaQkAAtA90ggj0JEEAtKVuQI",
"CAADAgADZAkAAtA90ghIMUWB17QRCwI",
"CAADAgADfwkAAtA90gjDt058XoEvtgI",
"CAADAgADhQkAAtA90gjDZ6ce4achkgI",
"CAADAgADiAkAAtA90ggKJgqu6MNtJgI",
"CAADAgADhwkAAtA90ghrLGOzFn5IPQI",
"CAADAgADjAkAAtA90giYSgd0Lc0XfgI",
"CAADAgADmwkAAtA90gjJzE_OmxbIxAI",
"CAADAgADpAkAAtA90ggPA6Ub6-K8bwI",
"CAADAgADIgoAAtA90ggGZNhsfS6sSAI",
"CAADAgAD4gMAAgk7OxMjOD_Q_B1mlwI",
"CAADAgAD5gMAAgk7OxP8aBy5isBhvAI",
"CAADAgADIQADd0tuHeya2GMEVo0kAg",
"CAADAgAD5wMAAgk7OxOsaUIDiDwsGgI",
"CAADAgADLQADcQnMBY5tMSxpt4DlAg",
"CAADAgADBQADcQnMBT-0NSPwLomkAg",
"CAADAgADGwADcQnMBbKc7P-CweEAAQI",
"CAADAgADIAADcQnMBWbYiJ5gr2s0Ag",
"CAADAgADKQADd0tuHXbILmh82o3UAg",
"CAADAgADHwADcQnMBZvG3UGwsgvSAg",
"CAADAgADDwADcQnMBUwKV2BryDpcAg",
"CAADAgADEAADcQnMBTHGOPNrv46tAg",
"CAADAgADBgADcQnMBZDodExqo1P1Ag",
"CAADAgADMAADcQnMBcKlhF3avezDAg",
"CAADAgADBQADcQnMBT-0NSPwLomkAg",
"CAADAgADBAADcQnMBRbnAAGHfnztqgI",
"CAADAgADAwADcQnMBSOApPq3qTrzAg",
"CAADAgADVgADd0tuHYRRApl4qdPBAg",
"CAADAgADDwIAAoqMcQNXvKuTBSGyUwI",
"CAADAgADwgEAAoqMcQPrsxD9MrytdgI",
"CAADAgADuAEAAoqMcQMsLiZiFlzzeQI",
"CAADAgADXgADd0tuHfqwcxc_Z7HNAg",
"CAADAgADqQEAAnwFBxtvT8tosL9NmgI",
"CAADAgAEAgACfAUHGztt3WLLgaWWAg",
"CAADAgADAQIAAnwFBxueu1I3JO5rLAI",
"CAADAgAD_gEAAnwFBxuB-iwTgB6gkAI",
"CAADAgAD-gEAAnwFBxsfuIdyaGJpSgI",
"CAADAgADEwIAAnwFBxv0IeWeCf7-bAI",
"CAADAgADFgIAAnwFBxsvVGMAAfgZUkMC",
"CAADAgADGgIAAnwFBxuMWIv10GfbfwI",
"CAADAgADcAADd0tuHWxDMymIcC8eAg",
"CAADAgADHQIAAnwFBxtVSQ_W7L0VsgI",
"CAADAgADHwIAAnwFBxuS3gNXUOy5bQI",
"CAADAgADeAADYIltDDNaGTClZLk6Ag",
"CAADAgADdAADYIltDCl8qrqhzWr8Ag",
"CAADAgADZwADYIltDBY8oH1rA7k-Ag",
"CAADAgADXgADYIltDJxjy_BT_xFPAg",
"CAADAgADVgADYIltDG1Zaxeo4oNSAg",
"CAADAgADUgADYIltDBp238_XJHBwAg",
"CAADAgADXAADYIltDAgZgYxjUpb6Ag",
"CAADAgADaQADYIltDEcxm7Lr5uVVAg",
"CAADAgADUQADd0tuHYBvFo0CHqfYAg",
"CAADAgADdgADYIltDBa8wdYY83w3Ag",
"CAADAgADLAADd0tuHd7y2wYnhfBYAg",
"CAADAgADnQAD8MPADjoWOSpb5g_0Ag",
"CAADAgADIgADd0tuHYmqCpNcuJKBAg",
"CAADAgADlgAD8MPADm9KogtSPIp5Ag",
"CAADAgADdAAD8MPADp40cadRIApfAg",
"CAADAgADgQAD8MPADj1a4tbu0ojpAg",
"CAADAgADHgADd0tuHbIP8sx9E5FSAg",
"CAADAgADyAAD8MPADuoMGYElZrvOAg",
"CAADAgADnAAD8MPADtkoD7-GtmJqAg",
"CAADAgADjAAD8MPADmVsEST5TboeAg",
"CAADAgADpgAD8MPADv8UZs0RBe8_Ag",
"CAADAgADzQAD8MPADpjPwOIIhDPOAg",
"CAADAgADEAADijc4AAESVXqKiwYE2wI",
"CAADAgADJwADijc4AAE3oUMhargOuAI",
"CAADAgADMwADijc4AAGU2NZK2N9ilwI",
"CAADAgADBAADijc4AAFx0NNqDnJm4QI",
"CAADAgADLQADijc4AAGBowxjAqAlGwI",
"CAADAgADFAADijc4AAGtl5dISqHmiAI",
"CAADAgADDAADd0tuHY0egk9b32EVAg",
"CAADAgADGwADijc4AAEdwByBSe9kgQI",
"CAADAgADEAIAAgk7OxP4kdl4KRtAsQI",
"CAADAgADGQIAAgk7OxMGxDHYj-pAqQI",
"CAADAgADHQIAAgk7OxOceY-EB-QP4wI",
"CAADAgADIgIAAgk7OxPu35kDt52eCgI",
"CAADAgADJgIAAgk7OxPhcJokb8Nr5gI",
"CAADAgADKAIAAgk7OxM3FgaI47btFwI",
"CAADAgADKAIAAgk7OxM3FgaI47btFwI",
"CAADAgADGAIAAgk7OxM08viZIZs9KwI",
"CAADAgADSwIAAgk7OxMqOlxxxqPpwwI",
"CAADAgADHwIAAgk7OxOA6jfhx16AIAI",
"CAADAgADIwIAAgk7OxNSKRy8v03MQAI",
"CAADAgADNAIAAgk7OxPjmrOOtMfVnwI",
"CAADAgADOQIAAgk7OxNqK1HedvTaBgI",
"CAADAgADPQIAAgk7OxNuyqa9W64WgAI",
"CAADAgADQQIAAgk7OxMv1gqf2nPTSQI",
"CAADAgADOwIAAgk7OxMwQSbVRE4LUQI",
"CAADAgADPwIAAgk7OxNHAAFzu3D5q0wC",
"CAADAgADQwIAAgk7OxPDZ4Shrgkd7wI",
"CAADAgADRwIAAgk7OxNmz5e6IX3wdQI",
"CAADAgADTgIAAgk7OxOp0cZnfUzzeAI",
"CAADAgADUAIAAgk7OxP1d56b3mcKQQI",
"CAADAgADngUAAkMj9gEj6pbXcHEW7wI",
"CAADAgADSgIAAgk7OxPEJg8eaHRwDwI",
"CAADAgADCQEAAmfUlg1wofftLMKkvAI",
"CAADAgADDgEAAmfUlg0xFMVzPb_U6QI",
"CAADAgADEgEAAmfUlg0du6cUVP-aHAI",
"CAADAgADnQUAAkMj9gEMZkCufUBgmAI",
"CAADAgADEwEAAmfUlg33lKTsw7nnAgI",
"CAADAgADDAEAAmfUlg0z5dT9cQM6_AI",
"CAADAgADFAEAAmfUlg1rEXCKaT_xYQI",
"CAADAgADHAEAAmfUlg2-0AKX2FGiqwI",
"CAADAgADHQEAAmfUlg04975CgyJXiAI",
"CAADAgADHwEAAmfUlg26WY23EhX7NAI",
"CAADAgADJQEAAmfUlg28koMyq69YzgI",
"CAADAgADOAEAAmfUlg1JG1mhqXm_6gI",
"CAADAgADIQEAAmfUlg1fEhUsWOzyHAI",
"CAADAgAD9QAD6gz8BlpxbZR_9BhMAg",
"CAADAgAD-gAD6gz8BtlO8EOup5j4Ag",
"CAADAgAD_wAD6gz8BujmGcDa-fiLAg",
"CAADAgADBAEAAuoM_AaurU3TvuZsFgI",
"CAADAgAD-AAD6gz8BoZ-rP8JJ1gDAg",
"CAADAgADAwEAAuoM_AZI6KfU7p9-CAI",
"CAADAgADUwMAAkcGQwXvNF-VQZCM3AI",
"CAADAgADnQIAAkcGQwUtRzGcvZoxhgI",
"CAADAgAD9gEAAkcGQwWaQirXk18k_gI",
"CAADAgAD_gEAAkcGQwWTzgABRUT1eBMC",
"CAADAgADBwADCcIkFzCtldSNwffpAg",
"CAADAgADBAIAAkcGQwX48VYjP9QhdQI",
"CAADAgAD8gEAAkcGQwXyEtgce5y-HQI",
"CAADAgAD6AEAAkcGQwUKwlCK9xAqogI",
"CAADAgAD5AEAAkcGQwWUTEz1z3Py5QI",
"CAADAgAD8AEAAkcGQwXM65dSwQaWrQI",
"CAADAgAEAgACRwZDBcBy4K6DeDjCAg",
"CAADAgADDAIAAkcGQwWzIY8WiUVbIQI",
"CAADAgADDAIAAkcGQwWzIY8WiUVbIQI",
"CAADAgADGAIAAkcGQwUt__vXE3QjRwI",
"CAADAgADIAIAAkcGQwV8ilH81BpFLgI",
"CAADAgADLAIAAkcGQwXRiwqXwUuCrwI",
"CAADAgADPgIAAkcGQwWI-bqLs-1SjAI",
"CAADAgADTgIAAkcGQwWU9HUs6JjbNgI",
"CAADAgADTAIAAkcGQwUJ1vTs62NfqgI",
"CAADAgADSAIAAkcGQwU-G-9SZUDTWAI",
"CAADAgADRgIAAkcGQwX7n5iviPuMJAI",
"CAADAgAD9gEAAkcGQwWaQirXk18k_gI",
"CAADAgADdgIAAkcGQwVZhA65_AGJRAI",
"CAADAgADsgEAAoqMcQPSoUoYgdT-fQI",
"CAADAgADmQIAAkcGQwWvSchVi_-YuAI",
"CAADAgADsAIAAkcGQwVRgj1wPWzs4QI",
"CAADAgADtAIAAkcGQwXJwFqZeAL-7QI",
"CAADAgADDAMAAkcGQwWgR8RIEVP9MgI",
"CAADAgADTwMAAkcGQwVZkX-Jo3i0TgI",
"CAADAgADXgMAAkcGQwXBWWOeOFmH6QI",
"CAADAgADiwMAAkcGQwWAlkz5p_mCQAI",
"CAADAgAEBQACRwZDBUlPNzl9SVJtAg",
"CAADAgADOhMAAp7OCwAB4dbw1ul97s4C",
"CAADAgADRBMAAp7OCwABkh3z-bvav-8C",
"CAADAgADbRMAAp7OCwABJkYQLPTVEkQC",
"CAADAgADdRMAAp7OCwABsgQZJNLTVxEC",
"CAADAgADdxMAAp7OCwABkl-Kye_JgzwC",
"CAADAgADQhMAAp7OCwAB_INFZpPZNK8C",
"CAADAgADxAEAAoqMcQMH8nTa_rMmTQI",
"CAADAgADUhMAAp7OCwABZqpWw-uxr1kC",
"CAADAgADcxMAAp7OCwABQ_0TfCsJlRcC",
"CAADAgADexMAAp7OCwABxgQ4PkhsNP4C",
"CAADAgADfRMAAp7OCwABs32igS5m9NMC",
"CAADAgADfxMAAp7OCwABKnNIbLi4O1EC",
"CAADAgADgRMAAp7OCwABl5qYC8ieP68C",
"CAADAgAD1wEAAoqMcQMF4GdwqWLCOAI",
"CAADAgADUBMAAp7OCwAB7I3VNk8kp6QC",
"CAADAgADkxMAAp7OCwABK6Zxz2jZLykC",
"CAADAgADpRMAAp7OCwAB0eQktfVTwesC",
"CAADAgAD0jAAAp7OCwAB1AiT9ng8udQC",
"CAADAgAD0zAAAp7OCwABvcz-hTyd0gcC",
"CAADAgAD6AEAAoqMcQMF37PHZMT57AI",
"CAADAgAD1zAAAp7OCwABlTe12EkTd6wC",
"CAADAgAD1jAAAp7OCwAC-V83-dA_lwI",
"CAADAgAD1TAAAp7OCwABgHY1XVnl_-4C",
"CAADAgAD1DAAAp7OCwABze-GefPG3MEC",
"CAADAgAD2DAAAp7OCwABs5_o-1GXN_0C",
"CAADAgAD2TAAAp7OCwAB8u0ep1vavl8C",
"CAADAgAD2jAAAp7OCwABZnsrxKjVx70C",
"CAADAgADixMAAp7OCwABrH0ToJWLXAQC",
"CAADAgADjRMAAp7OCwABAqHxKFOysIcC",
"CAADAgADjxMAAp7OCwABUdPTJDT3GtgC",
"CAADAgADkRMAAp7OCwABql8Ms1TPxeAC",
"CAADAgADTQADyJsDAAG6DcSDcxpKBAI",
"CAADAgADXQADyJsDAAHmXnaHEaSE7QI",
"CAADAgADXwADyJsDAAEDnOXAuebkBgI",
"CAADAgADaQADyJsDAAG3NoF1cpmzhQI",
"CAADAgADEQIAAoqMcQMKXPHnnhou4gI",
"CAADAgAD0gEAApkvSwrlguzA3-S_JgI",
"CAADAgADUAADmS9LCgneeMhlJCKvAg",
"CAADAgADVwsAApkvSwqCRp1xCiV_dwI",
"CAADAgADVgADmS9LCsEnIgOvKsnqAg",
"CAADAgADYgADmS9LCloe14FkpNDVAg",
"CAADAgADrwIAApkvSwp7MP3fawEYTgI",
"CAADAgADqwIAApkvSwoyKZ4cmA-DzAI",
"CAADAgADPAoAApkvSwrfwiiJ0Xq0FgI",
"CAADAgADgwADmS9LCstSM0J4upwuAg",
"CAADAgADqQIAApkvSwpApO3n69haxwI",
"CAADAgADBQEAApkvSwrgMoxF5v64fwI",
"CAADAgADYAADmS9LCgZxwtjtvXShAg",
"CAADAgADewADmS9LCkEObbhRaHn8Ag",
"CAADAgAD3QADmS9LCm0EVlxg21RqAg",
"CAADAgADsggAAgi3GQITL8y1531UoQI",
"CAADAgADnggAAgi3GQIAAa7bIj7XYTEC",
"CAADAgADpwgAAgi3GQL_22ABXC5rrgI",
"CAADAgAD2wgAAgi3GQJEsDHyi2NYRgI",
"CAADAgAD8wgAAgi3GQKHdYrrN-Wt_QI",
"CAADAgAD-AgAAgi3GQKArMM5DLCC-AI",
"CAADAgADtgEAAoqMcQMy71s6jPNdNwI",
"CAADAgADvgEAAoqMcQMVIo0PWbVwPQI",
"CAADAgADVwADZ1lbAAGRMVZUM9TkWQI",
"CAADAgADVQADZ1lbAAFkyhpXkXHxWAI",
"CAADAgADUwADZ1lbAAGdesPkSZW1qAI",
"CAADAgADnwADZ1lbAAHPrfRJcJP4-gI",
"CAADBQADgAMAAukKyAOXWG874z7K-AI",
"CAADBQADgQMAAukKyANDdDlhDY7IuQI",
"CAADBQADjgMAAukKyANXArxl3WaqUgI",
"CAADBQADlwMAAukKyAOTUOZzvxltnQI",
"CAADBQADtgMAAukKyAN_IGYzBDoeZwI",
"CAADBQADvgMAAukKyAO0kWldL75FSQI",
"CAADBQAD1QMAAukKyAM5DUnl41UtEwI",
"CAADBQAD2AMAAukKyANHCNzwa7LXjwI",
"CAADAgADOAADX8p-CzLiVfbJsCagAg",
"CAADAgADQQADX8p-C4WbElrPt_WIAg",
"CAADAgADLwADeXHeFgTLgXXciTG0Ag",
"CAADAgADEgADeXHeFr3kqKC9a0S1Ag",
"CAADAgADGgADOcGJDB5Q3upsdRDvAg",
"CAADAgADSioAAktqAwABYJfJOAN1P1MC",
"CAADAgADGgADOcGJDB5Q3upsdRDvAg",
"CAADAgADGwADOcGJDIWcNuzDZ_I-Ag",
"CAADAgADIQADOcGJDLQ3w2jzuv51Ag",
"CAADAgADHAADOcGJDCuZyoUAAd2nrwI",
"CAADBQADoAADDGCzCAK89a9v-EWbAg",
"CAADAgADHwADOcGJDN8zmJ_GUC4XAg",
"CAADAgADGgADOcGJDB5Q3upsdRDvAg",
"CAADAgADDQADQXbxIWhJeqsN7MDZAg",
"CAADAgADIAADOcGJDDp3qTonkx6oAg",
"CAADAgADjwYAAtJaiAEE4A-WIoMiBQI",
"CAADAgADJwADOcGJDLANeWLg8dTRAg",
"CAADAgADsAEAApzW5woQTw6kgPZX8wI",
"CAADBAADjQADAU-yB4IoNWJ8kHaHAg",
"CAADAgADGAADQXbxIRsIztEvvhXZAg",
"CAADAgADRgADQXbxIZVBMx9khOEmAg",
"CAADAgADIQQAArFfQQG00YxPXT7vKAI",
"CAADAgADiwYAAvoLtgj6ojzbjzVSFQI",
"CAADAgADlwEAAlrewQLGu3QbfiZ_WwI",
"CAADAgADOAADQXbxIY5H-8hlrMMhAg",
"CAADAgADmQEAAlrewQJW1HCU5ryO4wI",
"CAADAgADCwADQXbxIQZntRvjTodyAg",
"CAADAgADDAADQXbxIVZPT5cjKX-FAg",
"CAADAgADDQADQXbxIWhJeqsN7MDZAg",
"CAADAgADEQADQXbxIfdn8MpCobaLAg",
"CAADAgADEAADQXbxIe0EL8AL4IHQAg",
"CAADAgADFAADQXbxIXbZGJTPq3fPAg",
"CAADAgADEwADQXbxIRA2yz3V95UlAg",
"CAADAgADEgADQXbxIefKZlPvjWnbAg",
"CAADAgADFgADQXbxIaiaGpyCKT1XAg",
"CAADAgADGgADQXbxIUzASHT8HKGtAg",
"CAADAgADHgADQXbxIba7uqxFO3wRAg",
"CAADAgADHwADQXbxITZZ1lUJOx36Ag",
"CAADAgADpwEAAlrewQLHPz2LEWHVYQI",
"CAADAgADIAADQXbxIYHoLaWLztXDAg",
"CAADAgADQwADQXbxIaBAmzMdwj_NAg",
"CAADAgADSAADQXbxIS3lsJdqGV6kAg",
"CAADAgADTAADQXbxIZQMqE4GYVKFAg",
"CAADAgADSgADQXbxITST3rbefQIpAg",
"CAADAgADxQEAAlrewQK6XxZCcCpWewI",
"CAADAgADPwADOcGJDOAQTsIpoIXkAg",
"CAADAgADNAADOcGJDAWqy0xt_JdIAg",
"CAADAgADMAADOcGJDC7nYyYcKzUVAg",
"CAADAgADJwADOcGJDLANeWLg8dTRAg",
"CAADAgADGQQAArFfQQHNTpSJpoO58gI",
"CAADAgADFAQAArFfQQHN27RjdwmSAwI",
"CAADAgAD7gMAArFfQQHePYO9FvFnwwI",
"CAADAgAD6wMAArFfQQGW7yEXTBVAGgI",
"CAADBQADnAADDGCzCPUUYtEW362_Ag",
"CAADBQADSwADDGCzCJJt2E1vLx5kAg",
"CAADAgADQgIAAlrewQLFYDGIHyJDvgI",
"CAADBQADOgADDGCzCMmkztOd5l4qAg",
"CAADBQADagADDGCzCEELeFRja2SCAg",
"CAADBQADMAADDGCzCCgIkbyXL1nlAg",
"CAADBQADcgADDGCzCMKM-5PRlNCKAg",
"CAADBQADbwADDGCzCIzeoxprgMlLAg",
"CAADBQADeQADDGCzCAaU9XlyUwzMAg",
"CAADBQADpQADDGCzCAmGMR4_SzXWAg",
"CAADAgADKwADd0tuHakdSaLZcjYtAg",
"CAADAgADJwADd0tuHVXQmUr9NNwzAg",
"CAADAgADIwADd0tuHQVl0BBOiw2zAg",
"CAADAgADhQYAAvoLtghEkZGJldw8HgI",
"CAADAgADiwYAAvoLtgj6ojzbjzVSFQI",
"CAADAgADbQYAAvoLtghWC8kdPkyQbAI",
"CAADAgADbQYAAvoLtghWC8kdPkyQbAI",
"CAADBQADoAADDGCzCAK89a9v-EWbAg",
"CAADAgAD8wEAAmh9SAbmLMmkxlNy4gI",
"CAADAgAD8QEAAmh9SAZBDzhtssCbrwI",
"CAADAgAD6QEAAmh9SAbrt-PP8syOtAI",
"CAADAgAD-QEAAmh9SAa5R1ZJZwpgmwI",
"CAADBQADPAADDGCzCKIMr74QVp2UAg",
"CAADAgADbQIAAvilfQJ3ovLJ_da4ywI",
"CAADAgADbwIAAvilfQJdLfVNVLiGvwI"]

users = {}

class User:
    def __init__(self, id):
        self.id = id
        self.name = None
        self.age = None
        self.sex = None


TOKEN = '880951017:AAH30x9yHfvlrnojD1ONe11MD1vmkZkdkRk'
r = requests.get(f'https://api.telegram.org/bot{TOKEN}/getUpdates')

print(r.json())

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['help', 'start'])
def send_welcome(message: Message):
    user = User(message.from_user.id)
    users[message.from_user.id] = user
    user.name = str(message.from_user.first_name) + " " + str(message.from_user.last_name)
    bot.send_message(message.chat.id, f'Вот тебе первый стикер')
    bot.send_sticker(message.chat.id, random.choice(stickers))
    bot.send_message(message.chat.id, f"Привет, я бот! Тебя зовут \n{message.from_user.first_name} {message.from_user.last_name}?", reply_markup=gen_name_markup())


def gen_name_markup():
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(InlineKeyboardButton("Да, всё верно", callback_data="cb_yes"), InlineKeyboardButton("Нет", callback_data="cb_no"))
    return markup


def name_input(message: Message):
    # print(call.message)
    #  = message.from_user.id
    user = users[message.from_user.id]
    user.name = message.text
    bot.send_sticker(message.chat.id, random.choice(stickers))
    bot.send_message(message.chat.id, f'Отлично, {user.name}, вот тебе стикер')


@bot.inline_handler(lambda query: True)
def query_text(inline_query):
    # print(inline_query)
    try:
        r = types.InlineQueryResultArticle('1', inline_query.query, types.InputTextMessageContent(inline_query.query))
        r2 = types.InlineQueryResultArticle('2', inline_query.query[::-1], types.InputTextMessageContent(inline_query.query[::-1]))
        bot.answer_inline_query(inline_query.id, [r, r2])
    except Exception as e:
        print(e)
#
@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    try:
        user = users[call.from_user.id]
        if call.data == "cb_yes":
            bot.edit_message_reply_markup(message_id=call.message.message_id, chat_id=call.message.chat.id, reply_markup = None)
            bot.send_sticker(call.message.chat.id, random.choice(stickers))
            bot.send_message(call.message.chat.id, f'{user.name}, вот тебе стикер. Пиши что-нибудь, пришлю ещё')

        elif call.data == "cb_no":
            bot.edit_message_reply_markup(message_id=call.message.message_id, chat_id=call.message.chat.id, reply_markup = None)
            bot.send_message(call.message.chat.id, f'Безымянный, вот тебе стикер')
            bot.send_sticker(call.message.chat.id, random.choice(stickers))
            bot.send_message(call.message.chat.id, "Тогда введите ваше полное имя")
            bot.register_next_step_handler(call.message, name_input)
    except:
        send_welcome(call.message)

@bot.message_handler(content_types=['text'])
def color_choice(message: Message):
    # print(message)
    try:
        user = users[message.from_user.id]
        bot.send_sticker(message.chat.id, random.choice(stickers))
        bot.send_message(message.chat.id, f'{user.name}, вот тебе ЕЩЕ стикер')
    except:
        send_welcome(message)


@bot.message_handler(content_types=['sticker'])
def get_sticker(message: Message):
    bot.send_message(message.chat.id, f' вот тебе ЕЩЕ стикер')
    bot.send_sticker(message.chat.id, random.choice(stickers))
    print(message.sticker.file_id)
# # print()
#
#
# def gen_markup():
#     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
#     btn_black = types.KeyboardButton('Чёрный') #, callback_data=f"cb_black")
#     btn_white = types.KeyboardButton('Белый') #, callback_data=f"cb_white")
#     btn_yellow = types.KeyboardButton('Желтый') #, callback_data=f"cb_yellow")
#     markup.row(btn_black, btn_white, btn_yellow)
#     return markup
#
#
# def process_sex_step(message):
#     chat_id = message.chat.id
#     sex = message.text
#     if (sex == u'Чёрный') or (sex == u'Белый') or (sex ==u'Желтый'):
#         bot.send_message(chat_id, f"Nice to meet you, {sex}")
#     else:
#         raise Exception()
#
#
# @bot.message_handler(content_types=['text'])
# def msg_handler(message: Message):
#     reply = ""
#     if message.from_user.id in users:
#         reply += f"Ты мне уже писал. "
#     else:
#         reply += "Ты мне еще не писал. "
#     users.add(message.from_user.id)
#     # bot.send_message(message.chat.id, f'{reply}{message.from_user.first_name}, ты зачем мне шлешь "{message.text}"? Лучше стикер пришли')
#     f = open(r'users.pkl', 'wb')
#     pickle.dump(users, f)
#     f.close()
#     # reply_markup = gen_markup()
#     bot.send_message(message.chat.id, "Yes/no?", reply_markup=gen_markup())
#     process_sex_step(message)
#
#
# @bot.message_handler(content_types=['sticker'])
# def sticker_handler(message: Message):
#     bot.send_sticker(message.chat.id, random.choice(stickers))
#     bot.send_message(message.chat.id, f'Вот тебе тоже стикер. Шли еще')
#     print(message)
#     print(message.sticker)
#     # bot.reply_to(message, str(random.random()))
#
# @bot.inline_handler(lambda query: query.query == 'text')
# def query_text(inline_query):
#     try:
#         r = types.InlineQueryResultArticle('1', 'Result', types.InputTextMessageContent('Result message.'))
#         r2 = types.InlineQueryResultArticle('2', 'Result2', types.InputTextMessageContent('Result message2.'))
#         bot.answer_inline_query(inline_query.id, [r, r2])
#     except Exception as e:
#         print(e)
#
# @bot.message_handler(commands=['start', 'help'])
# def command_handler(message: Message):
#     bot.send_message(message.chat.id, f'Ты зачем мне шлешь команду "{message.text}" ')

# @bot.message_handler(content_types=['text'])
# def echo_digits(message: Message):
#     bot.reply_to(message, str(random.random()))


bot.polling(timeout=60)


# MAIN_URL = f'https://api.telegram.org/bot{TOKEN}'
# r = requests.get(f'{MAIN_URL}/getUpdates')
# print(r.json())


print('end')