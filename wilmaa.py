'''
    Wilmaa XBMC Plugin
    Copyright (C) 2014 stunna

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''
import xbmcgui, xbmcplugin
import resources.lib.feedparser as feedparser

plugin_handle = int(sys.argv[1])

def add_video_item(url, infolabels, img=''):
    listitem = xbmcgui.ListItem(infolabels['title'], iconImage=img, thumbnailImage=img)
    listitem.setInfo('video', infolabels)
    listitem.setProperty('IsPlayable', 'true')
    xbmcplugin.addDirectoryItem(plugin_handle, url, listitem, isFolder=False)

def get_epg(rss_url):
    feed = feedparser.parse( rss_url )
    prgtitle = []
    for i in range(0,len(feed['entries'])):
        prgtitle.append({
            'title': feed['entries'][i].title,
    })   
    return prgtitle

#load rss epg from swiss tv SRF
try:
    prgtitle = get_epg('http://tvprogramm.srf.ch/feed/q')
except Exception as e:
    log( "Exception: " + str(e))

#load rss programm info from tvspielfilm.de
try:
    prgtitle_spielfilm = get_epg('http://www.tvspielfilm.de/tv-programm/rss/jetzt.xml')
except Exception as e:
    log( "Exception: " + str(e))

#search for station name in epg information
def get_prgtitle(station, prgtitle, prgtitlespielfilm=''):
    i = len(prgtitle)-1
    while 0 < i:
        if prgtitle[i]['title'].find(station) > 0:
            return prgtitle[i]['title']
        i -= 1
    #search tv information on tvspielfilm if not found on SRF
    if i == 0:
        i2 = len(prgtitlespielfilm)-1
        while 0 < i2:
            print prgtitlespielfilm[i2]
            i2 -= 1
    return 'no information found'

#add stations to XBMC directory
base_url = 'http://iphone.wilmaa.com/iphone_channel/m3u8'
_id = 'plugin.video.wilmaa'
_resdir = "special://home/addons/" + _id + "/resources"

add_video_item('%s/%s.m3u8' % (base_url, 'ard'),{ 'title': 'ARD' + ' - ' + get_prgtitle('ARD:', prgtitle, prgtitle_spielfilm) }, '%s/media/ard.gif' % _resdir)
add_video_item('%s/%s.m3u8' % (base_url, 'zdf'),{ 'title': 'ZDF' + ' - ' + get_prgtitle('ZDF:', prgtitle, prgtitle_spielfilm) }, '%s/media/zdf.png' % _resdir)
add_video_item('%s/%s.m3u8' % (base_url, 'wdr'),{ 'title': 'WDR' + ' - ' + get_prgtitle('WDR:', prgtitle, prgtitle_spielfilm) }, '%s/media/wdr.png' % _resdir)
add_video_item('%s/%s.m3u8' % (base_url, 'sat1'),{ 'title': 'SAT1' + ' - ' + get_prgtitle('SAT1:', prgtitle, prgtitle_spielfilm) }, '%s/media/sat1.png' % _resdir)
add_video_item('%s/%s.m3u8' % (base_url, 'rtl'),{ 'title': 'RTL' + ' - ' + get_prgtitle('RTL:', prgtitle, prgtitle_spielfilm) }, '%s/media/rtl.png' % _resdir)
add_video_item('%s/%s.m3u8' % (base_url, 'rtl2'),{ 'title': 'RTL2' + ' - ' + get_prgtitle('RTL 2:', prgtitle, prgtitle_spielfilm) }, '%s/media/rtl2.jpg' % _resdir)
add_video_item('%s/%s.m3u8' % (base_url, 'pro7'),{ 'title': 'PRO7' + ' - ' + get_prgtitle('ProSieben CH::', prgtitle, prgtitle_spielfilm) }, '%s/media/pro7.png' % _resdir)
add_video_item('%s/%s.m3u8' % (base_url, 'vox'),{ 'title': 'VOX' + ' - ' + get_prgtitle('VOX:', prgtitle, prgtitle_spielfilm) }, '%s/media/vox.png' % _resdir)
add_video_item('%s/%s.m3u8' % (base_url, 'kabel_1'),{ 'title': 'Kabel1' + ' - ' + get_prgtitle('Kabel 1:', prgtitle, prgtitle_spielfilm) }, '%s/media/kabel1.png' % _resdir)
add_video_item('%s/%s.m3u8' % (base_url, 'dmax'),{ 'title': 'DMAX' + ' - ' + get_prgtitle('DMAX:', prgtitle, prgtitle_spielfilm) }, '%s/media/dmax.jpg' % _resdir)
add_video_item('%s/%s.m3u8' % (base_url, 'sixx'),{ 'title': 'Sixx' + ' - ' + get_prgtitle('Sixx:', prgtitle, prgtitle_spielfilm) }, '%s/media/sixx.jpg' % _resdir)
add_video_item('%s/%s.m3u8' % (base_url, 'dasvierte'),{ 'title': 'DasVierte' + ' - ' + get_prgtitle('DasVierte:', prgtitle, prgtitle_spielfilm) }, '%s/media/dasvierte.png' % _resdir)
add_video_item('%s/%s.m3u8' % (base_url, 'nickcc'),{ 'title': 'nickCC' + ' - ' + get_prgtitle('Nick/CC:', prgtitle, prgtitle_spielfilm) }, '%s/media/nickcc.png' % _resdir)
add_video_item('%s/%s.m3u8' % (base_url, 'superrtl'),{ 'title': 'SuperRTL' + ' - ' + get_prgtitle('Super RTL:', prgtitle, prgtitle_spielfilm) }, '%s/media/superrtl.png' % _resdir)
add_video_item('%s/%s.m3u8' % (base_url, 'viva'),{ 'title': 'Viva' + ' - ' + get_prgtitle('VIVA:', prgtitle, prgtitle_spielfilm) }, '%s/media/viva.png' % _resdir)
add_video_item('%s/%s.m3u8' % (base_url, 'n24'),{ 'title': 'N24' + ' - ' + get_prgtitle('N24:', prgtitle, prgtitle_spielfilm) }, '%s/media/n24.png' % _resdir)
add_video_item('%s/%s.m3u8' % (base_url, 'ntv'),{ 'title': 'NTV' + ' - ' + get_prgtitle('n-tv:', prgtitle, prgtitle_spielfilm) }, '%s/media/ntv.png' % _resdir)
add_video_item('%s/%s.m3u8' % (base_url, 'kika'),{ 'title': 'KIKA' + ' - ' + get_prgtitle('KIKA:', prgtitle, prgtitle_spielfilm) }, '%s/media/kika.png' % _resdir)
add_video_item('%s/%s.m3u8' % (base_url, 'sf1'),{ 'title': 'SRF1' + ' - ' + get_prgtitle('SRF 1:', prgtitle, prgtitle_spielfilm) }, '%s/media/srf1.png' % _resdir)
add_video_item('%s/%s.m3u8' % (base_url, 'sf2'),{ 'title': 'SRF2' + ' - ' + get_prgtitle('SRF zwei:', prgtitle, prgtitle_spielfilm) }, '%s/media/srf2.png' % _resdir)
add_video_item('%s/%s.m3u8' % (base_url, 'orf1'),{ 'title': 'ORF1' + ' - ' + get_prgtitle('ORF 1:', prgtitle, prgtitle_spielfilm) }, '%s/media/orf1.png' % _resdir)
add_video_item('%s/%s.m3u8' % (base_url, 'orf2'),{ 'title': 'ORF2' + ' - ' + get_prgtitle('ORF 2:', prgtitle, prgtitle_spielfilm) }, '%s/media/orf2.png' % _resdir)
add_video_item('%s/%s.m3u8' % (base_url, '3plus'),{ 'title': '3Plus' + ' - ' + get_prgtitle('3 plus:', prgtitle, prgtitle_spielfilm) }, '%s/media/3plus.png' % _resdir)
add_video_item('%s/%s.m3u8' % (base_url, 'arte_de'),{ 'title': 'ARTE(DE)' + ' - ' + get_prgtitle('ARTE:', prgtitle, prgtitle_spielfilm) }, '%s/media/arte.png' % _resdir)
add_video_item('%s/%s.m3u8' % (base_url, 'sfinfo'),{ 'title': 'SRFinfo' + ' - ' + get_prgtitle('SRF info:', prgtitle, prgtitle_spielfilm) }, '%s/media/srfinfo.png' % _resdir)
add_video_item('%s/%s.m3u8' % (base_url, '3sat'),{ 'title': '3SAT' + ' - ' + get_prgtitle('3sat:', prgtitle, prgtitle_spielfilm) }, '%s/media/3sat.png' % _resdir)
add_video_item('%s/%s.m3u8' % (base_url, 'zdfneo'),{ 'title': 'ZDFneo' + ' - ' + get_prgtitle('ZDFneo:', prgtitle, prgtitle_spielfilm) }, '%s/media/zdfneo.png' % _resdir)
add_video_item('%s/%s.m3u8' % (base_url, 'swr'),{ 'title': 'SWR' + ' - ' + get_prgtitle('SWR:', prgtitle, prgtitle_spielfilm) }, '%s/media/swr.png' % _resdir)
add_video_item('%s/%s.m3u8' % (base_url, 'br'),{ 'title': 'BR' + ' - ' + get_prgtitle('BR:', prgtitle, prgtitle_spielfilm) }, '%s/media/br.png' % _resdir)
add_video_item('%s/%s.m3u8' % (base_url, 'phoenix'),{ 'title': 'Phoenix' + ' - ' + get_prgtitle('phoenix:', prgtitle, prgtitle_spielfilm) }, '%s/media/phoenix.png' % _resdir)
add_video_item('%s/%s.m3u8' % (base_url, 'euronews'),{ 'title': 'Euronews' + ' - ' + get_prgtitle('Euronews:', prgtitle, prgtitle_spielfilm) }, '%s/media/euronews.png' % _resdir)
add_video_item('%s/%s.m3u8' % (base_url, 'eurosport'),{ 'title': 'Eurosport' + ' - ' + get_prgtitle('Eurosport:', prgtitle, prgtitle_spielfilm) }, '%s/media/eurosport.png' % _resdir)
add_video_item('%s/%s.m3u8' % (base_url, 'joiz'),{ 'title': 'JOIZ' + ' - ' + get_prgtitle('JOIZ:', prgtitle, prgtitle_spielfilm) }, '%s/media/joiz.png' % _resdir)
add_video_item('%s/%s.m3u8' % (base_url, 'rtlnitro'),{ 'title': 'RTLNitro' + ' - ' + get_prgtitle('RTLNITRO:', prgtitle, prgtitle_spielfilm) }, '%s/media/rtlnitro.png' % _resdir)
add_video_item('%s/%s.m3u8' % (base_url, 'servustv'),{ 'title': 'ServusTV' + ' - ' + get_prgtitle('ServusTV:', prgtitle, prgtitle_spielfilm) }, '%s/media/servustv.png' % _resdir)
add_video_item('%s/%s.m3u8' % (base_url, 'atv'),{ 'title': 'ATV' + ' - ' + get_prgtitle('ATV:', prgtitle, prgtitle_spielfilm) }, '%s/media/atv.png' % _resdir)
add_video_item('%s/%s.m3u8' % (base_url, 'cnn'),{ 'title': 'CNN' + ' - ' + get_prgtitle('CNN:', prgtitle, prgtitle_spielfilm) }, '%s/media/cnn.png' % _resdir)
add_video_item('%s/%s.m3u8' % (base_url, 'bbcworld'),{ 'title': 'BBCWorld' + ' - ' + get_prgtitle('BBCWorld:', prgtitle, prgtitle_spielfilm) }, '%s/media/bbcworld.png' % _resdir)
add_video_item('%s/%s.m3u8' % (base_url, 'tsr1'),{ 'title': 'RTS1' + ' - ' + get_prgtitle('RTS 1:', prgtitle, prgtitle_spielfilm) }, '%s/media/rts1.png' % _resdir)
add_video_item('%s/%s.m3u8' % (base_url, 'tsr2'),{ 'title': 'RTS2' + ' - ' + get_prgtitle('RTS 2:', prgtitle, prgtitle_spielfilm) }, '%s/media/rts2.png' % _resdir)
add_video_item('%s/%s.m3u8' % (base_url, 'tv5monde'),{ 'title': 'TV5Monde' + ' - ' + get_prgtitle('TV5Monde:', prgtitle, prgtitle_spielfilm) }, '%s/media/tv5monde.png' % _resdir)
add_video_item('%s/%s.m3u8' % (base_url, 'france2'),{ 'title': 'France2' + ' - ' + get_prgtitle('France2:', prgtitle, prgtitle_spielfilm) }, '%s/media/france2.png' % _resdir)
add_video_item('%s/%s.m3u8' % (base_url, 'france3'),{ 'title': 'France3' + ' - ' + get_prgtitle('France3:', prgtitle, prgtitle_spielfilm) }, '%s/media/france3.png' % _resdir)
add_video_item('%s/%s.m3u8' % (base_url, 'france5'),{ 'title': 'France5' + ' - ' + get_prgtitle('France5:', prgtitle, prgtitle_spielfilm) }, '%s/media/france5.png' % _resdir)
add_video_item('%s/%s.m3u8' % (base_url, 'rtl9'),{ 'title': 'RTL9' + ' - ' + get_prgtitle('RTL9:', prgtitle, prgtitle_spielfilm) }, '%s/media/rtl9.png' % _resdir)
add_video_item('%s/%s.m3u8' % (base_url, 'tf1'),{ 'title': 'TF1' + ' - ' + get_prgtitle('TF1:', prgtitle, prgtitle_spielfilm) }, '%s/media/tf1.png' % _resdir)
add_video_item('%s/%s.m3u8' % (base_url, 'm6'),{ 'title': 'M6' + ' - ' + get_prgtitle('M6:', prgtitle, prgtitle_spielfilm) }, '%s/media/m6.png' % _resdir)
add_video_item('%s/%s.m3u8' % (base_url, 'arte_fr'),{ 'title': 'ARTE(FR)' + ' - ' + get_prgtitle('ARTE:', prgtitle, prgtitle_spielfilm) }, '%s/media/arte.png' % _resdir)
add_video_item('%s/%s.m3u8' % (base_url, 'rsila1'),{ 'title': 'RSI1' + ' - ' + get_prgtitle('RSI 1:', prgtitle, prgtitle_spielfilm) }, '%s/media/rsila1.png' % _resdir)
add_video_item('%s/%s.m3u8' % (base_url, 'rsila2'),{ 'title': 'RSI2' + ' - ' + get_prgtitle('RSI 2:', prgtitle, prgtitle_spielfilm) }, '%s/media/rsila2.png' % _resdir)
add_video_item('%s/%s.m3u8' % (base_url, 'rai1'),{ 'title': 'Rai1' + ' - ' + get_prgtitle('Rai1:', prgtitle, prgtitle_spielfilm) }, '%s/media/rai1.png' % _resdir)
add_video_item('%s/%s.m3u8' % (base_url, 'rougetv'),{ 'title': 'RougeTV' + ' - ' + get_prgtitle('RougeTV:', prgtitle, prgtitle_spielfilm) }, '%s/media/rougetv.png' % _resdir)
add_video_item('%s/%s.m3u8' % (base_url, 'cartoonnetwork'),{ 'title': 'CartoonNetwork' + ' - ' + get_prgtitle('CartoonNetwork:', prgtitle, prgtitle_spielfilm) }, '%s/media/cartoonnetwork.png' % _resdir)
add_video_item('%s/%s.m3u8' % (base_url, 'latele'),{ 'title': 'LaTele' + ' - ' + get_prgtitle('LaTele:', prgtitle, prgtitle_spielfilm) }, '%s/media/latele.png' % _resdir)
add_video_item('%s/%s.m3u8' % (base_url, 'canal9'),{ 'title': 'Canal9' + ' - ' + get_prgtitle('Canal9:', prgtitle, prgtitle_spielfilm) }, '%s/media/canal9.png' % _resdir)
add_video_item('%s/%s.m3u8' % (base_url, 'canalalphaju'),{ 'title': 'CanalAlphaJU' + ' - ' + get_prgtitle('CanalAlphaJU:', prgtitle, prgtitle_spielfilm) }, '%s/media/canalalpha.png' % _resdir)
add_video_item('%s/%s.m3u8' % (base_url, 'tele1'),{ 'title': 'Tele1' + ' - ' + get_prgtitle('Tele1:', prgtitle)}, '%s/media/tele1.png' % _resdir)
add_video_item('%s/%s.m3u8' % (base_url, 'telem1west'),{ 'title': 'TeleM1West' + ' - ' + get_prgtitle('TeleM1West:', prgtitle, prgtitle_spielfilm) }, '%s/media/telem1.png' % _resdir)
add_video_item('%s/%s.m3u8' % (base_url, 'telem1ost'),{ 'title': 'TeleM1Ost' + ' - ' + get_prgtitle('TeleM1Ost:', prgtitle, prgtitle_spielfilm) }, '%s/media/telem1.png' % _resdir)
add_video_item('%s/%s.m3u8' % (base_url, 'teletoptg'),{ 'title': 'TeleTopTG' + ' - ' + get_prgtitle('TeleTopTG:', prgtitle, prgtitle_spielfilm) }, '%s/media/teletop.png' % _resdir)
add_video_item('%s/%s.m3u8' % (base_url, 'teletopzh'),{ 'title': 'TeleTopZH' + ' - ' + get_prgtitle('TeleTopZH:', prgtitle, prgtitle_spielfilm) }, '%s/media/teletop.png' % _resdir)
add_video_item('%s/%s.m3u8' % (base_url, 'teletopsh'),{ 'title': 'TeleTopSH' + ' - ' + get_prgtitle('TeleTopSH:', prgtitle, prgtitle_spielfilm) }, '%s/media/teletop.png' % _resdir)
add_video_item('%s/%s.m3u8' % (base_url, 'canalalphane'),{ 'title': 'CanalAlphaNE' + ' - ' + get_prgtitle('CanalAlphaNE:', prgtitle, prgtitle_spielfilm) }, '%s/media/canalalpha.png' % _resdir)
add_video_item('%s/%s.m3u8' % (base_url, 'teleticino'),{ 'title': 'TeleTicino' + ' - ' + get_prgtitle('TeleTicino:', prgtitle, prgtitle_spielfilm) }, '%s/media/teleticino.png' % _resdir)
add_video_item('%s/%s.m3u8' % (base_url, 'telebasel'),{ 'title': 'TeleBasel' + ' - ' + get_prgtitle('TeleBasel:', prgtitle, prgtitle_spielfilm) }, '%s/media/telebasel.png' % _resdir)
add_video_item('%s/%s.m3u8' % (base_url, 'e4'),{ 'title': 'E4' + ' - ' + get_prgtitle('E4:', prgtitle, prgtitle_spielfilm) }, '%s/media/e4.png' % _resdir)
add_video_item('%s/%s.m3u8' % (base_url, 'lemanbleu'),{ 'title': 'lemanbleu' + ' - ' + get_prgtitle('lemanbleu:', prgtitle, prgtitle_spielfilm) }, '%s/media/lemanbleu.jpg' % _resdir)
add_video_item('%s/%s.m3u8' % (base_url, 'film4'),{ 'title': 'Film4' + ' - ' + get_prgtitle('Film4:', prgtitle, prgtitle_spielfilm) }, '%s/media/film4.jpg' % _resdir)

xbmcplugin.endOfDirectory(plugin_handle)