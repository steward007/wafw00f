#!/usr/bin/env python
'''
Copyright (C) 2019, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

# NOTE: this priority list is used so that each check can be prioritized,
# so that the quick checks are done first and ones that require more
# requests, are done later


wafdetectionsprio = [
    'XLabs Security WAF (XLabs)',
    'Kona Site Defender (Akamai)',
    'ACE XML Gateway (Cisco)',
    'aeSecure (aeSecure)',
    'AireeCDN (Airee)',
    'Airlock (Phion/Ergon)',
    'Alert Logic (Alert Logic)',
    'AliYunDun (Alibaba Cloud Computing)',
    'Anquanbao (Anquanbao)',
    'AnYu (AnYu Technologies)',
    'Approach (Approach)',
    'AppWall (Radware)',
    'Armor Defense (Armor)',
    'ArvanCloud (ArvanCloud)',
    'ASP.NET Generic Protection (Microsoft)',
    'ASPA Firewall (ASPA Engineering Co.)',
    'Astra Web Protection (Czar Securities)',
    'AzionCDN (AzionCDN)',
    'Barikode (Ethic Ninja)',
    'Barracuda Application Firewall (Barracuda Networks)',
    'Bekchy (Faydata Technologies Inc.)',
    'Beluga CDN (Beluga)',
    'BIG-IP Local Traffic Manager (F5 Networks)',
    'BinarySec (BinarySec)',
    'BitNinja (BitNinja)',
    'BlockDoS (BlockDoS)',
    'Bluedon (Bluedon IST)',
    'BulletProof Security Pro (AITpro Security)',
    'CacheWall (Varnish)',
    'CacheFly CDN (CacheFly)',
    'Comodo cWatch (Comodo CyberSecurity)',
    'CdnNS Application Gateway (CdnNs/WdidcNet)',
    'ChinaCache CDN Load Balancer (ChinaCache)',
    'Chuang Yu Shield (Yunaq)',
    'Cloudbric (Penta Security)',
    'Cloudflare (Cloudflare Inc.)',
    'Cloudfloor Application Firewall (Cloudfloor DNS)',
    'Cloudfront (Amazon)',
    'CrawlProtect (Jean-Denis Brun)',
    'DataPower (IBM)',
    'DenyALL (Rohde & Schwarz CyberSecurity)',
    'Distil (Distil Networks)',
    'DOSarrest (DOSarrest Internet Security)',
    'DotDefender (Applicure Technologies)',
    'DynamicWeb Injection Check (DynamicWeb)',
    'Edgecast (Verizon Digital Media)',
    'Eisoo Cloud Firewall (Eisoo)',
    'Expression Engine (EllisLab)',
    'e3Learning Firewall',
    'BIG-IP Application Security Manager (F5 Networks)',
    'BIG-IP Access Policy Manager (F5 Networks)',
    'Fastly CDN (Fastly)',
    'FirePass (F5 Networks)',
    'FortiWeb (Fortinet)',
    'GoDaddy Website Protection (GoDaddy)',
    'Greywizard (Grey Wizard)',
    'HyperGuard (Art of Defense)',
    'Imunify360 (CloudLinux)',
    'Incapsula (Imperva Inc.)',
    'IndusGuard (Indusface)',
    'Instart DX (Instart Logic)',
    'ISA Server (Microsoft)',
    'Janusec Application Gateway (Janusec)',
    'Jiasule (Jiasule)',
    'KS-WAF (KnownSec)',
    'KeyCDN (KeyCDN)',
    'LiteSpeed Firewall (LiteSpeed Technologies)',
    'LimeLight CDN (LimeLight)',
    'Open-Resty Lua Nginx',
    'Oracle Cloud (Oracle)',
    'Malcare (Inactiv)',
    'MaxCDN (MaxCDN)',
    'Mission Control Application Shield (Mission Control)',
    'ModSecurity (SpiderLabs)',
    'NAXSI (NBS Systems)',
    'Nemesida (PentestIt)',
    'NevisProxy (AdNovum)',
    'NetContinuum (Barracuda Networks)',
    'NetScaler AppFirewall (Citrix Systems)',
    'Newdefend (NewDefend)',
    'NexusGuard Firewall (NexusGuard)',
    'NinjaFirewall (NinTechNet)',
    'NullDDoS Protection (NullDDoS)',
    'NSFocus (NSFocus Global Inc.)',
    'OnMessage Shield (BlackBaud)',
    'Palo Alto Next Gen Firewall (Palo Alto Networks)',
    'PerimeterX (PerimeterX)',
    'PentaWAF (Global Network Services)',
    'pkSecurity Intrusion Detection System',
    'Positive Technologies Application Firewall (PT Security)',
    'PowerCDN (PowerCDN)',
    'Profense (ArmorLogic)',
    'Puhui (Puhui)',
    'Qiniu (Qiniu CDN)',
    'Reblaze (Reblaze)',
    'RSFirewall (RSJoomla!)',
    'ASP.NET RequestValidationMode (Microsoft)',
    'Safe3 Web Firewall (Safe3)',
    'Safedog (SafeDog)',
    'Safeline (Chaitin Tech.)',
    'SecKing (SecKing)',
    'eEye SecureIIS (BeyondTrust)',
    'SecuPress WordPress Security (SecuPress)',
    'SecureSphere (Imperva Inc.)',
    'Secure Entry (United Security Providers)',
    'SEnginx (Neusoft)',
    'ServerDefender VP (Port80 Software)',
    'Shield Security (One Dollar Plugin)',
    'Shadow Daemon (Zecure)',
    'SiteGround (SiteGround)',
    'SiteGuard (Sakura Inc.)',
    'Sitelock (TrueShield)',
    'SonicWall (Dell)',
    'UTM Web Protection (Sophos)',
    'Squarespace (Squarespace)',
    'SquidProxy IDS',
    'StackPath (StackPath)',
    'Sucuri CloudProxy (Sucuri Inc.)',
    'Tencent Cloud Firewall (Tencent Technologies)',
    'Teros (Citrix Systems)',
    'Trafficshield (F5 Networks)',
    'TransIP Web Firewall (TransIP)',
    'URLMaster SecurityCheck (iFinity/DotNetNuke)',
    'URLScan (Microsoft)',
    'UEWaf (UCloud)',
    'Varnish (OWASP)',
    'Viettel (Cloudrity)',
    'VirusDie (VirusDie LLC)',
    'Wallarm (Wallarm Inc.)',
    'WatchGuard (WatchGuard Technologies)',
    'WebARX (WebARX Security Solutions)',
    'WebKnight (AQTRONIX)',
    'WebLand (WebLand)',
    'RayWAF (WebRay Solutions)',
    'WebSEAL (IBM)',
    'WebTotem (WebTotem)',
    'West263 Content Delivery Network',
    'Wordfence (Defiant)',
    'WP Cerber Security (Cerber Tech)',
    'WTS-WAF (WTS)',
    '360WangZhanBao (360 Technologies)',
    'Xuanwudun',
    'Yundun (Yundun)',
    'Yunsuo (Yunsuo)',
    'Yunjiasu (Baidu Cloud Computing)',
    'YXLink (YxLink Technologies)',
    'Zenedge (Zenedge)',
    'ZScaler (Accenture)'
]
