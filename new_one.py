from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException
from datetime import datetime
import pandas as pd
import time, os, re
import logging
from datetime import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException, TimeoutException, NoSuchElementException
import time

# system_links = ['https://www.myfxbook.com/members/Raminpegana/amir-hossein-yazdanfar-puma/9441467', 'https://www.myfxbook.com/members/fxsumo/fx-sumo-diversified-portfolio/9869912', 'https://www.myfxbook.com/members/HappyForex/happy-gold-eightcap-m30/10281851', 'https://www.myfxbook.com/members/kyuirori/oldhearth-ea02-2/9374810', 'https://www.myfxbook.com/members/Dampel/eternity/9135123', 'https://www.myfxbook.com/members/Dampel/eternity-by-freddy/9306786', 'https://www.myfxbook.com/members/IBLFX/9528-ibl-original-hanjido/10965394', 'https://www.myfxbook.com/members/Sirapattt/st02magen3-ex%E0%B9%82%E0%B8%8A%E0%B8%84%E0%B8%94%E0%B8%A1%E0%B8%8A%E0%B8%A2-%E0%B9%82%E0%B8%8A%E0%B8%84%E0%B8%8A%E0%B8%A2%E0%B8%A1%E0%B8%A7%E0%B8%A7/10448452', 'https://www.myfxbook.com/%22/members/Qwerty2022/%22', 'https://www.myfxbook.com/members/0msTrade/0mstrade-zzzzz-fff666/7032072', 'https://www.myfxbook.com/members/alex_forex2024/100-accuracy-gold-only/11128678', 'https://www.myfxbook.com/members/sawyer_h/100000yen-challenge/7605216', 'https://www.myfxbook.com/members/leopin/159031143/9140196', 'https://www.myfxbook.com/members/aisaba/2020-00/7601776', 'https://www.myfxbook.com/members/www35/2022-westernpips--private-7/9412468', 'https://www.myfxbook.com/members/Mkplr1/24-hr-rsi-discretionary/9275501', 'https://www.myfxbook.com/members/vshmonov/3-profit-fx321/3617787', 'https://www.myfxbook.com/members/NimsaraDon/30-master-aka-sniper/10752934', 'https://www.myfxbook.com/members/MillsRymer/310200294/8777717', 'https://www.myfxbook.com/members/3ton_io/3ton-enhanced-alpha-30/9726950', 'https://www.myfxbook.com/members/vshmonov/4-profit-fx321/3615560', 'https://www.myfxbook.com/members/Valentincassani/426/8132849', 'https://www.myfxbook.com/members/Natawun/46013378/3335854', 'https://www.myfxbook.com/members/Mateo10mp/500usd/7468022', 'https://www.myfxbook.com/members/yunben/536371/2413233', 'https://www.myfxbook.com/members/fxzenko/78034725-agold/10889754', 'https://www.myfxbook.com/members/coymahrens/930760/7638071', 'https://www.myfxbook.com/members/Ravengroup2/6ftr-06/3208652', 'https://www.myfxbook.com/members/fjkdlenw123/-/7549617', 'https://www.myfxbook.com/members/tung1610/simple-breakout/10244313', 'https://www.myfxbook.com/%22/members/ongpchye/%22', 'https://www.myfxbook.com/%22/members/KingStrategy2021/%22', 'https://www.myfxbook.com/members/metry/abt-cross-v1/9766557', 'https://www.myfxbook.com/members/azreemohamad/acc-usd1000/8283755', 'https://www.myfxbook.com/members/kreafx/account-dl-ea-1/9410527', 'https://www.myfxbook.com/members/kreafx/account-tb-ea-1/6415052', 'https://www.myfxbook.com/members/firelazi/acnestis/9585628', 'https://www.myfxbook.com/members/acoesfacil/acoesfacil/10391232', 'https://www.myfxbook.com/members/tizianob/activetrades25-1/8565855', 'https://www.myfxbook.com/members/EURONIS/activtrades--euroniscom-mt5-v1331/9427979', 'https://www.myfxbook.com/members/arponirep/aeg17i-%D0%BC%D0%B0%D1%80%D1%82-2020/4832700', 'https://www.myfxbook.com/members/leo23/agi-ea-v11-real-account/9794445', 'https://www.myfxbook.com/%22/members/Agustincalvo/%22', 'https://www.myfxbook.com/members/ahmedzubair/ahmed-zubair-dhaiban-aldhaif/3205751', 'https://www.myfxbook.com/members/0963/ais-unhinged/11040677', 'https://www.myfxbook.com/members/Frinx/aizack-friend/9419981', 'https://www.myfxbook.com/members/albumariusiulian/albumariusiulian/3509808', 'https://www.myfxbook.com/members/Michail91/alc-70519/3574281', 'https://www.myfxbook.com/members/TM2021/alfa-advisor/10527437', 'https://www.myfxbook.com/members/GeorGabeev/alfainvest/9168838', 'https://www.myfxbook.com/members/AOSPrisma/algoforex-1/8374502', 'https://www.myfxbook.com/members/AOSPrisma/algoforex-3/8439582', 'https://www.myfxbook.com/%22/members/algofxmoney/%22', 'https://www.myfxbook.com/members/Knaiiff/ali-abdallah/11103547', 'https://www.myfxbook.com/members/Kamyar_rc/ali-kasb-100/11075116', 'https://www.myfxbook.com/members/alinikafrouz/ali-nikafrouz-real/10968228', 'https://www.myfxbook.com/members/RenatoTakahashi/all-trading/9574093', 'https://www.myfxbook.com/members/Scrittore/alpari-ecn/3538933', 'https://www.myfxbook.com/members/fxalphaalgo/alpha-ic-markets/11142240', 'https://www.myfxbook.com/members/FCAcademyTS/alpha-libertex/9230050', 'https://www.myfxbook.com/members/EasonLyon/alpha-masterclass-march-ea/8038986', 'https://www.myfxbook.com/members/FxGuardianz/alpha-prime-c/7924027', 'https://www.myfxbook.com/members/PhoenixStrategy/alphafx/10374060', 'https://www.myfxbook.com/members/mastermind4242/alphatrader/8391355', 'https://www.myfxbook.com/members/DiegoTrader02/alvaro-hart/9328917', 'https://www.myfxbook.com/members/Forexpanda/alvina/7617199', 'https://www.myfxbook.com/%22/members/AlyceFx/%22', 'https://www.myfxbook.com/members/Insome93/amazing-light-standart-aggressive/9308415', 'https://www.myfxbook.com/members/SwapsRollovers/amega-macro-trading-usd-short/11016806', 'https://www.myfxbook.com/members/AndorraTrading25/andorra-trading-ai-elite/11111423', 'https://www.myfxbook.com/members/AndorraTrading25/andorra-trading-pack-1-d/10397428', 'https://www.myfxbook.com/members/mrAntonio/annic/10442687', 'https://www.myfxbook.com/%22/members/ap_trader/%22', 'https://www.myfxbook.com/%22/members/DonaldRay/%22', 'https://www.myfxbook.com/members/ARCCO/arc/7618788', 'https://www.myfxbook.com/members/beachtrader/arca-maxx-1/8665969', 'https://www.myfxbook.com/members/Gotmog/argo/9695907', 'https://www.myfxbook.com/members/EAAIFX/artificial-intelligence/10748993', 'https://www.myfxbook.com/members/AbeYue/asalbiruclose/10009155', 'https://www.myfxbook.com/members/AbeYue/asalbiruclose-mt5/10710131', 'https://www.myfxbook.com/members/ascapitaltrading/asct-163003157/11067829', 'https://www.myfxbook.com/members/ProjectXFX/asterysc-hunter-1/2992420', 'https://www.myfxbook.com/members/ProjectXFX/asterysc-hunter-2/5847056', 'https://www.myfxbook.com/members/XMforextrader/atp-micro-jmc5107/10235079', 'https://www.myfxbook.com/members/paulinobsp/aurum-meum/9661990', 'https://www.myfxbook.com/members/autobotapp/autobot-ai-power-trading-high/10381187', 'https://www.myfxbook.com/members/AutoBot2021/autobot2021-ea/9499456', 'https://www.myfxbook.com/members/antonovea/automated-longterm/8605547', 'https://www.myfxbook.com/members/sawyer_h/ava-live/3349355', 'https://www.myfxbook.com/members/pitufogranjero/axi/2322201', 'https://www.myfxbook.com/members/ayant78/ayant/9324007', 'https://www.myfxbook.com/members/befusion/bas-axi/9951721', 'https://www.myfxbook.com/members/Pijitr/bbands-cent/3506529', 'https://www.myfxbook.com/members/BEPROFITFX/be-profit-fx/11152522', 'https://www.myfxbook.com/members/majdan/become-more-2/7514512', 'https://www.myfxbook.com/members/DIM_trade/belkaglazer-icmarkets/4382719', 'https://www.myfxbook.com/members/BigGlobalCapital/big-global-currency-fund-1/10662979', 'https://www.myfxbook.com/members/hongkong6429/black-cat/9386473', 'https://www.myfxbook.com/members/jmlaas/blackbird-10/6447866', 'https://www.myfxbook.com/members/Blacknumbrs/blacknumbrs-mam/9497771', 'https://www.myfxbook.com/members/doctor_manakova/bloomx/10879207', 'https://www.myfxbook.com/%22/members/BlueJackPro/%22', 'https://www.myfxbook.com/members/bossbuu/boss-usdc/11096068', 'https://www.myfxbook.com/members/fedechevalier/bot-forex-2/9135085', 'https://www.myfxbook.com/members/DizFix/bot2-581-neomod1/3270892', 
# 'https://www.myfxbook.com/members/DizFix/bot3-978-neoagr/3564720', 'https://www.myfxbook.com/members/EJBackes/brcopy130-multix/10721574', 'https://www.myfxbook.com/members/EJBackes/brcopy900-multix/10721598', 'https://www.myfxbook.com/members/sixth_sense/breakthrough-strategy-icm/3631372', 'https://www.myfxbook.com/%22/members/Xtine77/%22', 'https://www.myfxbook.com/members/FaisalWahyu/brother/10043711', 'https://www.myfxbook.com/members/MischenkoValeria/btc-pepper-2/9459776', 'https://www.myfxbook.com/members/beachtrader/btc-tomec/7558465', 'https://www.myfxbook.com/members/MischenkoValeria/btc-trading-pepper/9728099', 'https://www.myfxbook.com/members/niveshcrypto/btc-cfg-245785/8378671', 'https://www.myfxbook.com/members/bencoolentrader/bunghamzah/10845220', 'https://www.myfxbook.com/members/LWSH6688/butterfly-hedge-1/9772998', 'https://www.myfxbook.com/members/AH852/cap-eurusd-10002-h1-dup/10444520', 'https://www.myfxbook.com/members/lambdavictory/carakita/11049321', 'https://www.myfxbook.com/members/beharapfx/cent/7568531', 'https://www.myfxbook.com/members/Axion_fx/cetus/11163600', 'https://www.myfxbook.com/members/CarlFX88/cfx-xs-project/11011882', 'https://www.myfxbook.com/members/Profitcamp/champion-ea/10407631', 'https://www.myfxbook.com/members/YogiKotecha/chandu-1/7629351', 'https://www.myfxbook.com/members/chaikhaodee/charoenchai/10058345', 'https://www.myfxbook.com/members/willemvdingh/chart-chaser/11112524', 'https://www.myfxbook.com/members/HossanaChikwado/chikwado-fx/8332231', 'https://www.myfxbook.com/members/allenhihi/cjrcent5/7967267', 'https://www.myfxbook.com/members/Cisar/ckm/9318171', 'https://www.myfxbook.com/members/Maximilian777/clever-v/10609109', 'https://www.myfxbook.com/members/sergklyuev/client-005/7941280', 
# 'https://www.myfxbook.com/members/sergklyuev/client-010/8111254', 'https://www.myfxbook.com/members/TriumphFxVietnam/cloud-data-cd-trader/5247940', 'https://www.myfxbook.com/members/vesbolt1/cloudtrader/10610943', 'https://www.myfxbook.com/members/Cologne_Trading/cologne-ultra-poker/9749944', 'https://www.myfxbook.com/members/lingkon38/consistant-profit/11050893', 'https://www.myfxbook.com/members/forexaries/contingency/6206828', 'https://www.myfxbook.com/members/Hydra_MrRobot/copy-trade/3569855', 'https://www.myfxbook.com/members/ONEG00DGUY/copyfx-roboforex/11062518', 'https://www.myfxbook.com/members/CopyMyPips/copymypips-pamm-01/10581202', 'https://www.myfxbook.com/members/azreemohamad/copytrade-usd100-gmiedge/7393341', 'https://www.myfxbook.com/members/EMOforex/copytrademaster/8291714', 'https://www.myfxbook.com/members/Corvex/corvex-capital-mam/8398205', 'https://www.myfxbook.com/members/CR7EA/cr7ea-crypto/9624236', 'https://www.myfxbook.com/members/CR7EA/cr7ea-vip-safe-setting/11094361', 'https://www.myfxbook.com/members/CR7EA/cr7ea-vip-safe-setting/11004350', 'https://www.myfxbook.com/members/crownetrades/crownetrades/9146449', 'https://www.myfxbook.com/members/AlgocratAI/crypto-portfolio/10729251', 'https://www.myfxbook.com/members/cryptowized/cryptorunner-btc-eth/11057159', 'https://www.myfxbook.com/members/Tharsay/cthu/9301513', 'https://www.myfxbook.com/members/mik1790/currencystrategy/10161991', 'https://www.myfxbook.com/members/Raazim/daily-ai-trading-kraitosx-raidar/10774675', 'https://www.myfxbook.com/members/dd1983/dario-main-account/10513092', 'https://www.myfxbook.com/members/LongVision/darwin-tvs/3575530', 'https://www.myfxbook.com/members/thedreams/datis/11100625', 'https://www.myfxbook.com/members/ManiTrading2013/davolucasmt5/8902164', 'https://www.myfxbook.com/members/Exploration60/dax-special/8975103', 'https://www.myfxbook.com/members/DAXMEISTER/daxmeister/9138704', 'https://www.myfxbook.com/members/MayconGuedes/decocopybmavolumeeaforex/9167070', 'https://www.myfxbook.com/members/balloontong/demand-supply-by-tp/9386521', 'https://www.myfxbook.com/members/MY_INVEST/dev-rock/10645284', 'https://www.myfxbook.com/members/MY_INVEST/dev-sky/10645225', 'https://www.myfxbook.com/members/BunnySingh/dgn-k/9581014', 'https://www.myfxbook.com/members/dikyzhuo/diky-nas100/4740314', 'https://www.myfxbook.com/members/lensk/dima-vip-bot-0721/8592611', 'https://www.myfxbook.com/members/FERRARI2009/disco-fibo-pamm/9493882', 'https://www.myfxbook.com/members/Mkplr1/discretionary/3348474', 'https://www.myfxbook.com/members/BautistaGagliano/diversified-multiple-ea-portfolio/11043786', 'https://www.myfxbook.com/members/MonsterKing/dm-fx-exness/9278175', 'https://www.myfxbook.com/members/richman789/doodee-raptor-mini/11042864', 'https://www.myfxbook.com/members/Deepocketsystem/dps/3985973', 'https://www.myfxbook.com/members/Alex72tyumen/dragon-trade-x5/9426318', 'https://www.myfxbook.com/members/dreamads/dreamads/7945983', 'https://www.myfxbook.com/members/Ivan24/dreamcatcher/5550865', 'https://www.myfxbook.com/members/PoonpitiSalakit/dreams-come-true/9387795', 'https://www.myfxbook.com/members/NickOosten/dutchforexinvestments/10089309', 'https://www.myfxbook.com/members/FelipeDutra/dutrader/8702957', 'https://www.myfxbook.com/members/diver_cp/dxt-h1/7921894', 'https://www.myfxbook.com/members/Phuttiwong/ea-candle-exness-1hr/10073753', 'https://www.myfxbook.com/members/Tifel/ea-euro/8592816', 'https://www.myfxbook.com/members/wiextreme/ea-glory-75/11136357', 'https://www.myfxbook.com/members/HTServices/ea-ht-evolution/6526079', 'https://www.myfxbook.com/members/HTServices/ea-ht-evolution-mt5/7444663', 'https://www.myfxbook.com/members/HTServices/ea-ht-fusion-v2/6526087', 'https://www.myfxbook.com/members/HTServices/ea-ht-mix-prom5/6525998', 'https://www.myfxbook.com/members/HTServices/ea-ht-plus/6526060', 'https://www.myfxbook.com/members/SatrioAdhi/ea-id-pro/9308348', 'https://www.myfxbook.com/members/onederic/ea-mr-micro-me-bet/7432800', 'https://www.myfxbook.com/members/poploveaye/ea-richmachine-gold/8827809', 'https://www.myfxbook.com/members/tranthai0101/ea-scalping-profit-15month/8600969', 'https://www.myfxbook.com/members/Idalina/ea-supergrid/9311035', 'https://www.myfxbook.com/%22/members/EAPH2022/%22', 'https://www.myfxbook.com/members/eafiltergrid/eafg-190304/10188767', 'https://www.myfxbook.com/members/Balltro/eagle-high-risk/11136493', 'https://www.myfxbook.com/members/EagleAI/eagle-ultimate/10250171', 'https://www.myfxbook.com/members/DelMare/earningseason/9813551', 'https://www.myfxbook.com/members/AMAP/ea-robo-forex-gratis/9797264', 'https://www.myfxbook.com/members/eladaforex/elada-fibo-64/3560952', 'https://www.myfxbook.com/members/ElderCustodians/eldercus/8121957', 'https://www.myfxbook.com/members/TopRank/elite-forex-scalper/11102084', 'https://www.myfxbook.com/members/felixbaksafx/eliteforexscalper2021/9136318', 'https://www.myfxbook.com/members/empirefx1/empire-fx--mosallam/10479885', 'https://www.myfxbook.com/members/Enlightenedtrade/enlightened-forest-ranger/9041764', 'https://www.myfxbook.com/members/Enlightenedtrade/enlightened-life--forrest-ranger/8901156', 'https://www.myfxbook.com/members/ayman30/equiti-fahad-live1/3531541', 'https://www.myfxbook.com/members/Dharamjeet/eshan-440293634-just/10741474', 'https://www.myfxbook.com/members/TipakornPandee/espm-auc/9315049', 'https://www.myfxbook.com/members/TipakornPandee/espm-auc2/9315052', 'https://www.myfxbook.com/members/TipakornPandee/espm-auc3/9315054', 'https://www.myfxbook.com/members/TipakornPandee/espm-auc4/9315065', 'https://www.myfxbook.com/members/Dampel/eternity-500-cent/9244953', 'https://www.myfxbook.com/members/alsenna/ethusd-btcusd-solusd/9340482', 'https://www.myfxbook.com/members/VEERAPHAT/eu-%E0%B8%9E%E0%B8%AD%E0%B8%95%E0%B9%80%E0%B8%A5%E0%B8%81/8857111', 'https://www.myfxbook.com/members/MayconGuedes/eumanualxm/9167122', 'https://www.myfxbook.com/members/eurgenerator/eur-generator-51453436/11096555', 'https://www.myfxbook.com/members/Dermawanderder/euro-scalper-v1/11078264', 'https://www.myfxbook.com/members/AlejandroGigena/europa-1/10842156', 'https://www.myfxbook.com/members/ProspectIInvest/europa-fx-mr/9562363', 'https://www.myfxbook.com/members/eaforexglobal/expertsniperx-pioneer-account-jg3036/11057473', 'https://www.myfxbook.com/members/Answer13/extreme-20/10064999', 'https://www.myfxbook.com/members/eZanFx/ezanfx-nzdusd/10063092', 'https://www.myfxbook.com/members/Alcad83/fair-signal/5387387', 'https://www.myfxbook.com/members/Nandoboom78/fats-target-2-monthly/9741221', 'https://www.myfxbook.com/members/fxdothacker/fbs-cx-prima/7948255', 'https://www.myfxbook.com/members/eddhl89/fbs-2021/9466695', 'https://www.myfxbook.com/members/Tofuhead/fbs-oil-x2-dual-grid/10349454', 'https://www.myfxbook.com/members/nampee/fbs230497314/9788802', 'https://www.myfxbook.com/%22/members/Adnanzahid2009/%22', 'https://www.myfxbook.com/members/test_bigmon_fx/fdentn2655/7463757', 'https://www.myfxbook.com/members/RomanNikolaevich/fd-xtrem-cent-manual/10990368', 'https://www.myfxbook.com/members/Fernando01/fer150/8692353', 'https://www.myfxbook.com/members/Fernando01/fer668/9139388', 'https://www.myfxbook.com/members/fernando11/fernando-trader/6550139', 
# 'https://www.myfxbook.com/%22/members/ForexDrive2024/%22', 'https://www.myfxbook.com/members/HMTC/fightant100usd/10612098', 'https://www.myfxbook.com/members/Mkplr1/finch-11/3363612', 'https://www.myfxbook.com/members/Mkplr1/finch-241/3339087', 'https://www.myfxbook.com/members/klasterer/finch-live/3739895', 'https://www.myfxbook.com/members/vetallnemo/firmum-fiduciam-motus/1584377', 'https://www.myfxbook.com/members/smangusts/fix-fly-test/8692683', 'https://www.myfxbook.com/members/Enlightenedtrade/flfx-c75/9313220', 'https://www.myfxbook.com/members/gepards/fluctuate/9499402', 'https://www.myfxbook.com/members/wayaneka/follow-trend/9717906', 'https://www.myfxbook.com/members/HendraSaputra/fookin-eejit/9927447', 'https://www.myfxbook.com/members/Enlightenedtrade/forest-ranger-fp-markets/9206320', 'https://www.myfxbook.com/members/alanproject/forex-cyborg-high-risk/7872037', 'https://www.myfxbook.com/members/forexdiamond/forex-diamond-real-money/3402799', 'https://www.myfxbook.com/members/fxgoldinvestor/forex-gold-investor-real/6541429', 'https://www.myfxbook.com/members/Taveesak/forex-quanteas--group/9153844', 'https://www.myfxbook.com/members/kokillennium/forexous-safe/11024565', 'https://www.myfxbook.com/members/SwapsRollovers/fp-markets-news-tradingrisk-events/11018593', 'https://www.myfxbook.com/members/Dinasl/fte-robot/10226431', 'https://www.myfxbook.com/members/fxmoneymakers/fund-management/11098334', 'https://www.myfxbook.com/members/linhthatsat/fx-path/10882381', 'https://www.myfxbook.com/members/FXSCALPERX/fx-scalper-4x--standard/10312396', 'https://www.myfxbook.com/members/nickdarcfx/fxchoice/9442314', 'https://www.myfxbook.com/members/sst_trader/fxcm-mara/8695681', 'https://www.myfxbook.com/members/ayman30/fxdd-ayman-live2/4757156', 'https://www.myfxbook.com/members/ayman30/fxdd-ayman-live3/4757016', 'https://www.myfxbook.com/members/ayman30/fxdd-talal-live1/4758241', 'https://www.myfxbook.com/members/nikdom99/fxrunner/9437484', 'https://www.myfxbook.com/members/nguyen94/fxtm-2891030-6pairs-004lots/7620223', 'https://www.myfxbook.com/members/nguyen94/fxtm-2940965-eurgbp-005lots/8394799', 'https://www.myfxbook.com/members/nguyen94/fxtm-2946053-eurusd-005lots/8398107', 'https://www.myfxbook.com/members/nguyen94/fxtm-2954226-nzdusd-005lots/8394874', 'https://www.myfxbook.com/members/JHancox/fxtp-youtube/9156188', 'https://www.myfxbook.com/members/schmartin/fxwolf-grid/7624152', 'https://www.myfxbook.com/members/schmartin/fxwolf-professional/9839145', 'https://www.myfxbook.com/members/FX_Advance/fx-advance/10200636', 'https://www.myfxbook.com/members/Cornerstone1/gain-dao-beta/7670587', 'https://www.myfxbook.com/members/TheCapital/gc-investment/10904043', 'https://www.myfxbook.com/members/GCICS/gcics-avatrade/11063220', 'https://www.myfxbook.com/members/gchristin/gc-short-n-09/10047225', 'https://www.myfxbook.com/members/scnintertrade/gd-ai-10k-gmi/10458506', 'https://www.myfxbook.com/members/mareclinho/gearbox-mt4/10981645', 'https://www.myfxbook.com/members/Tony66/gearbox-real-5000/7701433', 'https://www.myfxbook.com/members/GENERALIFX/generalifx-falcon-gcmai/10973922', 'https://www.myfxbook.com/members/Marrkdy/gerard-genius-ea/10410260', 'https://www.myfxbook.com/members/arkkaraart/gj-eu-swing-trade/10535128', 'https://www.myfxbook.com/members/GLGroup/glgroup-capital/9680512', 'https://www.myfxbook.com/members/Ramss999/global-range/2551932', 'https://www.myfxbook.com/members/Maasysarfx/gmi-10000/9315399', 'https://www.myfxbook.com/members/SeksanExness8838/gmi-6477-jade-kale-gridbeta/10941221', 'https://www.myfxbook.com/members/aofwittawat/gmi-rsi-hedge/10185443', 'https://www.myfxbook.com/members/grantlow/gmmav1/7967325', 'https://www.myfxbook.com/members/INFINITUMPRO/gnescomp/10504609', 'https://www.myfxbook.com/members/ArkusFx/gold--eu/9453952', 'https://www.myfxbook.com/members/SimpleistheBest/gold-02-simpleisthebest/11149729', 'https://www.myfxbook.com/%22/members/pietpuk/%22', 'https://www.myfxbook.com/%22/members/Jeffsek/%22', 'https://www.myfxbook.com/members/DesignatedTrader/gold-digger-fbs/8590769', 'https://www.myfxbook.com/members/Profitcamp/gold-dragon-ea/9679283', 'https://www.myfxbook.com/%22/members/skillforex/%22', 'https://www.myfxbook.com/members/MyGoldTrend/gold-trend-strategy/9343797', 'https://www.myfxbook.com/members/andyyong8881/gold-hunder-hedge/8414760', 'https://www.myfxbook.com/members/future74/goldalgo/11100652', 'https://www.myfxbook.com/members/tarunads/golden-action/9889762', 'https://www.myfxbook.com/members/atlantisvn/golden-buffalo-channel-rate/10936554', 'https://www.myfxbook.com/members/xixitrading/golden-era-pamm/10570758', 'https://www.myfxbook.com/members/Sergeyr5/goldenbot-live/7270604', 'https://www.myfxbook.com/members/GoldenEdgeEA/goldenedge-ea/11159756', 'https://www.myfxbook.com/members/khodzhaev/goldentradingclassic/8809518', 'https://www.myfxbook.com/members/zv735/goldmind-cs-kzm/2259132', 'https://www.myfxbook.com/members/LightInvest/goldpill/10464369', 'https://www.myfxbook.com/members/nawafxbooks/goldstar-system-v2/11164454', 'https://www.myfxbook.com/members/hokuto/good-morning-ultimate-tradeview-ecn/6418746', 'https://www.myfxbook.com/members/teitan/gp1/10572160', 'https://www.myfxbook.com/members/GreenBotEA/greenbotscalperpro/10230163', 'https://www.myfxbook.com/members/LeilaWilliams/greezly/9855219', 'https://www.myfxbook.com/members/SmartInvestition/groshyk/11133893', 'https://www.myfxbook.com/members/phillonguyen/gto-pro/10517291', 'https://www.myfxbook.com/members/Pijitr/halfgrid-cent/3599515', 'https://www.myfxbook.com/%22/members/TradingHinvest/%22', 'https://www.myfxbook.com/members/handy_systems/handy-systems-real-investment/10943482', 'https://www.myfxbook.com/members/HappyForex/happy-breakout-vtmarkets/9607500', 'https://www.myfxbook.com/members/HappyForex/happy-gold-tmgm-m30/9375654', 'https://www.myfxbook.com/members/HappyForex/happy-gold-vtmarkets-m30/8647517', 'https://www.myfxbook.com/members/harapansukses/harapan-ayang/10917789', 'https://www.myfxbook.com/members/hassiikahloon/haseeb-hk3/10165993', 'https://www.myfxbook.com/members/Zex47/hawkeye-leix-01/11059141', 'https://www.myfxbook.com/members/Rodrixxx/hedge-fund-ai-2/9702200', 'https://www.myfxbook.com/members/Akadech/heding-model1/8327503', 'https://www.myfxbook.com/members/felip_martinez08/heidy-escudero-investing/9170845', 'https://www.myfxbook.com/members/atlantisvn/hermes-speed/11062741', 'https://www.myfxbook.com/members/TheTradingMaster/hft-thetradingmaster/11053154', 'https://www.myfxbook.com/members/HIamHiamAlgo/hiamhiam-algo-1/8771340', 'https://www.myfxbook.com/members/EKFX/high-frequency-strategy/9522209', 'https://www.myfxbook.com/members/hikooki424/hikooki424/10415412', 'https://www.myfxbook.com/members/hizeiris/hizevantage/10665554', 'https://www.myfxbook.com/members/PHAMVOVUONGHOANG/hoangforex-com/11012640', 'https://www.myfxbook.com/members/fxpodoz/howard/8671051', 'https://www.myfxbook.com/members/Rufathakimov/h-rufeek/9343172', 'https://www.myfxbook.com/members/iBotForex/ibot-edith-27113151/8763304', 'https://www.myfxbook.com/members/FERRARI2009/ic-markets/3534905', 'https://www.myfxbook.com/members/me156695/ic-markets-live/3299297', 'https://www.myfxbook.com/members/SwapsRollovers/ic-markets-macro-trading-usd/11016873', 'https://www.myfxbook.com/members/hmacedo/icm-manual-mt4-2000034723/4196981', 'https://www.myfxbook.com/members/forallatlantis/icm-vc-eur/9153124', 'https://www.myfxbook.com/members/tranle447/ic-aud/1191686', 'https://www.myfxbook.com/members/syafeeq/iea/10996039', 'https://www.myfxbook.com/members/IlBossDelTrading/il-boss-del-trading-scalper/10565721', 'https://www.myfxbook.com/members/mrdanquah/im-mastery-account/9425085', 'https://www.myfxbook.com/members/CTudor/ina-mari-conciu-conciu-tudor/9767245', 'https://www.myfxbook.com/members/forexstore/incontrol/2624558', 'https://www.myfxbook.com/members/forexstore/incontrol-usdcad/10579631', 'https://www.myfxbook.com/members/Urytomsk/inquisitor-pro/9820786', 'https://www.myfxbook.com/members/sofiansyah/insta-5235/7579555', 'https://www.myfxbook.com/members/eurgenerator/instaforex-51453274/11096530', 'https://www.myfxbook.com/members/itsvp/investax--icmarketssc-live-/10183077', 'https://www.myfxbook.com/members/itsvp/investax--icmarketssc-live-/10092632', 'https://www.myfxbook.com/members/FXTGFund/investing-geometry/4758171', 'https://www.myfxbook.com/members/jabed777/investor-38/9365795', 'https://www.myfxbook.com/members/danithiam/investors/10704029', 'https://www.myfxbook.com/members/ishikawalab/ishikawarobot-1/9717505', 'https://www.myfxbook.com/members/1turnQ/issarah-xm/9378480', 'https://www.myfxbook.com/members/haku777/issen-10-001/7602326', 'https://www.myfxbook.com/members/ITSPride/its-pride-092021/10959001', 'https://www.myfxbook.com/members/ITSPride/its-pride-102021/10959106', 'https://www.myfxbook.com/members/Oleg047/ivolga99/9746225', 'https://www.myfxbook.com/members/WIPHEA/izanagi-20/9167654', 'https://www.myfxbook.com/members/javierdario76/javier-gold-scalper-mt5/11104531', 'https://www.myfxbook.com/members/Javiernator/javiernator-company/8591915', 'https://www.myfxbook.com/members/eonejaws/jawsfx/8926376', 'https://www.myfxbook.com/members/dhkc8848/jd-888-scalper-cash-out/8981662', 'https://www.myfxbook.com/members/Jhonfxx/jhonfx/10929140', 'https://www.myfxbook.com/members/jjeswanth/jkown/9323684', 'https://www.myfxbook.com/members/JamesJGevana/joanna-liteforex/9329592', 'https://www.myfxbook.com/members/jded/jonnars-micro-account-v1/10482653', 'https://www.myfxbook.com/members/JoyJoy735/joy-fix4/9437680', 'https://www.myfxbook.com/%22/members/MheejJR/%22', 
# 'https://www.myfxbook.com/%22/members/MheejJR/%22', 'https://www.myfxbook.com/members/Tannim/kazi-tanjedul-ershad/3477109', 'https://www.myfxbook.com/members/Kaztian/kaztian-forex--easy/11146246', 'https://www.myfxbook.com/members/kobebrian/kb-funny-oil-tmgm/11150305', 'https://www.myfxbook.com/members/mt4easystemtrade/khs-3000-s20-titanfx-01/1914305', 'https://www.myfxbook.com/%22/members/RM92/%22', 'https://www.myfxbook.com/members/kintoyyy/kintoyyy-xm/9331260', 'https://www.myfxbook.com/members/ksrufx/kiril-fxopen-auznzd-rp5/9389059', 'https://www.myfxbook.com/members/eawealthythai/kittipat-8213571-vt-markets/8589499', 'https://www.myfxbook.com/members/eawealthythai/komsil-8213773-vt-markets/8590695', 'https://www.myfxbook.com/members/ASTek/konserva/10874324', 'https://www.myfxbook.com/members/Dermawanderder/kontest-1/11057517', 'https://www.myfxbook.com/members/Auiam/kritsada/9117168', 'https://www.myfxbook.com/members/Kudou/kudou2/2631932', 'https://www.myfxbook.com/members/Infincomru/kurs-invest/11080173', 'https://www.myfxbook.com/members/neter1987/lastchancemyson/7901367', 'https://www.myfxbook.com/members/Chaiyaporn_P/legion-k-tapthai/8384302', 'https://www.myfxbook.com/members/forextraffic/lem-3-99-sl/9892000', 'https://www.myfxbook.com/members/Leonetrading/leonetrading-strategy/11059247', 'https://www.myfxbook.com/%22/members/AleDily82/%22', 'https://www.myfxbook.com/members/mastergary/ling-ling-strategy-m200/11007465', 'https://www.myfxbook.com/members/Drolph/litforce/6061998', 'https://www.myfxbook.com/members/Pusakaru/live-nov-17-2024/10714032', 'https://www.myfxbook.com/members/Sophieann/live1/7180451', 'https://www.myfxbook.com/members/Yoyo85/lk-1/11079192', 'https://www.myfxbook.com/members/LPiton/longterminvest/7949084', 'https://www.myfxbook.com/members/LotialBullion/lotialbullion-ea-xxiii/10663487', 'https://www.myfxbook.com/members/EAAIFX/low-dd-eaaifx/11095572', 'https://www.myfxbook.com/members/richowl007/low-risk-mid-return-long/9311102', 'https://www.myfxbook.com/members/HungMinh/lucky/9326446', 'https://www.myfxbook.com/members/LynxTrading/lynxsolutions--1x-private/10775811', 'https://www.myfxbook.com/members/ota_0626_2019/ma3-sv01-108-8961/3394297', 'https://www.myfxbook.com/members/akkradet/macdrsistoch-27kusc-111131445/10962234', 'https://www.myfxbook.com/members/MuhdArrif/mamr-96-trading/9567153', 'https://www.myfxbook.com/members/ManuelPacer/manuel-scalper/9888636', 'https://www.myfxbook.com/members/Makafton/marina-baymakova/7477797', 'https://www.myfxbook.com/members/forexstore/market-fighter/8227972', 'https://www.myfxbook.com/members/Forexpanda/marlon/7779483', 'https://www.myfxbook.com/members/MayconGuedes/marloncopybmavolumeeaforex/9167054', 'https://www.myfxbook.com/members/TradingIQ/marshcapitalmgmt/3968123', 'https://www.myfxbook.com/members/JakovM/martnmultym/2750132', 'https://www.myfxbook.com/members/nextleveltryout/master/10717181', 'https://www.myfxbook.com/members/Mastertraderist/master-hk50-port1/11120232', 'https://www.myfxbook.com/members/bangozz83/masto/9026805', 'https://www.myfxbook.com/members/MattBezo/matt-bezo/10250571', 'https://www.myfxbook.com/members/MattiaBellesso/mattia-bellesso/10188924', 'https://www.myfxbook.com/members/Mayte/mayte-real-icmarkets/10748589', 'https://www.myfxbook.com/members/nekiy/melbourne-money-box-ecn/9467200', 'https://www.myfxbook.com/members/Joelopenshaw/mg-pro-v1/9169760', 'https://www.myfxbook.com/members/migoninvest/migon-invest/7458946', 'https://www.myfxbook.com/members/LiamForexTrader/miracle/9516899', 'https://www.myfxbook.com/members/MM_Trading/mm-trading/10163899', 'https://www.myfxbook.com/members/Matteopolito/mmtrading/10259930', 'https://www.myfxbook.com/members/indiaking1/mondal-superfast-scalping/11093324', 'https://www.myfxbook.com/members/MoneyMakersEA/money-makers-ea-v30/9865667', 'https://www.myfxbook.com/members/TeodorchikFest/moneymaker/2240613', 'https://www.myfxbook.com/members/jeffho1992/monkeyking/10189869', 'https://www.myfxbook.com/members/Moon_and_Star/moonstar1/7434872', 'https://www.myfxbook.com/members/Moon_and_Star/moonstar3/8181933', 'https://www.myfxbook.com/members/Francesco7304/mosquito-ea/11028751', 'https://www.myfxbook.com/members/vanj10227/mp-forex-pro-account-management/9004461', 'https://www.myfxbook.com/members/sendbad/mt4-186719/3562679', 'https://www.myfxbook.com/members/BrickmanKevin/mt4-70034869/10756368', 'https://www.myfxbook.com/members/Supermario7/mt4-7316892/8676938', 'https://www.myfxbook.com/members/MarketLikeAGirl/mt4-8377574/9292987', 'https://www.myfxbook.com/members/Kovanis/mt4-874512/10551317', 'https://www.myfxbook.com/members/NguyenHuyTrung/mt4-893924/6988532', 'https://www.myfxbook.com/members/special_hp/mt4-ic-3k-230079086-ecn/10057529', 'https://www.myfxbook.com/members/fiatelpis2/mt4-fiatelpis/8397278', 'https://www.myfxbook.com/members/bocs/mt5-5104737/3532117', 'https://www.myfxbook.com/members/bocs/mt5-5106645/3533990', 'https://www.myfxbook.com/members/bocs/mt5-5124964/3685050', 'https://www.myfxbook.com/members/serg150115/mt5-5412530/9337375', 'https://www.myfxbook.com/members/edswin/mtsfbs-ea-public-account/9316270', 'https://www.myfxbook.com/members/AlgoLab/mt-ai-x2-crypto/10870752', 'https://www.myfxbook.com/members/ArcLab/multi-star-c/9290782', 'https://www.myfxbook.com/members/paveludo/multiwaystrait-mt5-roboforex/11079632', 'https://www.myfxbook.com/members/Emilfrank/my-first-work/10804632', 'https://www.myfxbook.com/%22/members/LinoCapital/%22', 'https://www.myfxbook.com/members/Narcis141183/narcis141183/4438334', 'https://www.myfxbook.com/%22/members/Cuiriz/%22', 'https://www.myfxbook.com/members/Viacheslav1212/natali/10917804', 'https://www.myfxbook.com/members/Dampel/neuro-20k/9135601', 'https://www.myfxbook.com/members/Neverdie_TH/never-die-th/10918981', 'https://www.myfxbook.com/members/ngkarsoon/ng-kar-soon-fbs-euraud/6952055', 'https://www.myfxbook.com/members/ngkarsoon/ng-kar-soon-fbs-gbpaud/7464456', 'https://www.myfxbook.com/members/ngkarsoon/ng-kar-soon-fbs-gbpusd/6952041', 'https://www.myfxbook.com/members/ngkarsoon/ng-kar-soon-micro-gbpusd/7464443', 
# 'https://www.myfxbook.com/members/ngkarsoon/ng-kar-soon-40k-portfolio/8733426', 'https://www.myfxbook.com/members/tradingsvietnam/nguyenminhtam/9847129', 'https://www.myfxbook.com/members/MischenkoValeria/night-hunter-best-pairs-minpricerange/9729305', 'https://www.myfxbook.com/members/MischenkoValeria/night-hunter-pro-3-pairs/8584715', 'https://www.myfxbook.com/members/MischenkoValeria/night-hunter-pro-all-pairs/8562210', 'https://www.myfxbook.com/members/MischenkoValeria/night-hunter-pro-best-pairs/8562205', 'https://www.myfxbook.com/members/MischenkoValeria/night-hunter-pro-extreme-mt5/9378437', 'https://www.myfxbook.com/members/MischenkoValeria/night-hunter-pro-pepper/9485101', 'https://www.myfxbook.com/members/Linhforex/night-scalp-only-icm-ecn/10780551', 'https://www.myfxbook.com/members/dvrk78/nightvisionea-mt5/7449501', 'https://www.myfxbook.com/members/Nikita1992/nikita/9150454', 'https://www.myfxbook.com/members/FCAcademyTS/nobelportolio-agressive/6521685', 'https://www.myfxbook.com/members/FCAcademyTS/nobelportolio-moderate/6521755', 'https://www.myfxbook.com/members/nomadfulcrum/nomad-fulcrum-quant-agrressive/10339010', 'https://www.myfxbook.com/members/tec_daniel/nopain-mt5/11204017', 'https://www.myfxbook.com/members/nqueiros/nqueiros-mt5-std/5374528', 'https://www.myfxbook.com/members/NorthAcademy/o-segredo-gringo/9339803', 'https://www.myfxbook.com/members/NorthAcademy/o-segredo-gringo-estrat%C3%A9gia-prata/9339989', 'https://www.myfxbook.com/members/m1800/o6b--ic-marketsxx873/2139608', 'https://www.myfxbook.com/members/m1800/o6b--ic-marketsxx986/2633250', 'https://www.myfxbook.com/members/hyderfox/oanda--tradingview-hedging-1/7902664', 'https://www.myfxbook.com/members/pipatoh/oh-ho/7386886', 'https://www.myfxbook.com/members/omfxservices/omfx-eurusd/10808121', 'https://www.myfxbook.com/members/IVT2020/way/6383781', 'https://www.myfxbook.com/members/az_whye/ophiuchus/6493135', 'https://www.myfxbook.com/members/optinskijj/optinskii/10737986', 'https://www.myfxbook.com/members/optinskijj/optinskii-an/11133795', 'https://www.myfxbook.com/members/pitikcilik/p4pum4/9245296', 
# 'https://www.myfxbook.com/members/m6776609234/pa2247/8559489', 'https://www.myfxbook.com/members/kreafx/panther-ea-1/5552272', 'https://www.myfxbook.com/members/kreafx/panther-ea-3/7275378', 'https://www.myfxbook.com/%22/members/jasma23/%22', 'https://www.myfxbook.com/members/thaicentermall/passive-ant/10350702', 'https://www.myfxbook.com/members/Stefanofx66/pendbot-v991/11059185', 'https://www.myfxbook.com/members/hmacedo/pepper-manual-mt5-51013387/4399449', 'https://www.myfxbook.com/%22/members/likklekev21/%22', 'https://www.myfxbook.com/members/phuked/perfect-ea/10214932', 'https://www.myfxbook.com/members/bastdost/pescado/8340868', 'https://www.myfxbook.com/members/PhanK/phan-ki%C3%AAn/10893203', 'https://www.myfxbook.com/members/proGlobalTrader/pimpyourtrading/7385829', 'https://www.myfxbook.com/members/pipsmen/pipsmen-defensive/8597177', 'https://www.myfxbook.com/members/sinthununpop/pobmt4/5229215', 'https://www.myfxbook.com/members/Beside39/pondo-ohji-axiory-nano/8559361', 'https://www.myfxbook.com/members/Pierstage_CM/portfolio-6/7573066', 'https://www.myfxbook.com/members/PorfolioFX/portfoliofx-eurusd/10548410', 'https://www.myfxbook.com/members/leapfx/power-growth-trader/10536828', 'https://www.myfxbook.com/members/natachavimolsub/poysignologomt4/9326685', 'https://www.myfxbook.com/members/meydow/print-dollar-price-action-ea/9514831', 'https://www.myfxbook.com/members/TfxEvolution/pro-golg-ecn/11153721', 'https://www.myfxbook.com/%22/members/QuantumEuro/%22', 'https://www.myfxbook.com/members/Profit_Pro/profit-pro-turbo/10553132', 'https://www.myfxbook.com/members/FxAddict/project-2022/9316906', 'https://www.myfxbook.com/members/SwapsRollovers/purple-trading-macro-trading-usd/11018621', 'https://www.myfxbook.com/members/xoro1987/qiwix-tm-sn/9481372', 'https://www.myfxbook.com/members/master_255/qm-type2/1876475', 'https://www.myfxbook.com/members/PashaZverev/quantum-business/10519566', 'https://www.myfxbook.com/members/atlantisvn/quantum-hermes/11050602', 'https://www.myfxbook.com/members/atlantisvn/quantum-speed/10984634', 'https://www.myfxbook.com/members/Answer13/quattro-pro-auto/6552985', 'https://www.myfxbook.com/members/johnmacknamara/r-factor-fxopen/9237967', 'https://www.myfxbook.com/members/johnmacknamara/r-factor-1-hour-per/8331290', 'https://www.myfxbook.com/members/johnmacknamara/r-factor-custom/9366736', 'https://www.myfxbook.com/members/johnmacknamara/r-factor-extended-w-sonic/8332293', 'https://www.myfxbook.com/members/johnmacknamara/r-factor-jm-portfolio/8365278', 'https://www.myfxbook.com/members/johnmacknamara/r-factor-last-15/8331302', 'https://www.myfxbook.com/members/johnmacknamara/r-factor-portfolio-mean-reversal/8016551', 'https://www.myfxbook.com/%22/members/ronin47/%22', 'https://www.myfxbook.com/members/Ramabhakta/rama-gld-trump-100-50/3619824', 'https://www.myfxbook.com/members/tesmatt/realfx/8401160', 'https://www.myfxbook.com/members/strategyworks/realtimeforexsignalscom/4965490', 'https://www.myfxbook.com/members/plane1959/retirement-fund/6414356', 'https://www.myfxbook.com/members/nekiy/reykjavik-money-box-ecn/9320150', 'https://www.myfxbook.com/members/Reza_Wallstreet/rezawallstreet/10449225', 'https://www.myfxbook.com/members/johnmacknamara/rfactor-eurcad-high-risk/2611161', 'https://www.myfxbook.com/members/BLZRobots/rf-hrtrump/3520572', 'https://www.myfxbook.com/%22/members/GabryFX/%22', 'https://www.myfxbook.com/members/sethlondon/rh-xm-global--euroniscom/9389008', 'https://www.myfxbook.com/members/rhyspalmer/rhys-palmer-icm/9156647', 'https://www.myfxbook.com/members/richrom/richrom-manhatten/7926932', 'https://www.myfxbook.com/members/ali982222/risky/10250094', 'https://www.myfxbook.com/members/sumantri76/rizal/9679917', 'https://www.myfxbook.com/members/sailorbg/robo-usd-prime/8392328', 'https://www.myfxbook.com/members/Traderbot/roboforex-%D1%80%D0%B0%D0%B7%D0%B3%D0%BE%D0%BD-cs-400/11074913', 'https://www.myfxbook.com/members/leocabral84/rob%C3%B4s-exness/5950558', 'https://www.myfxbook.com/members/BusinessHome_pro/robotforex-pro-ecn/10178204', 'https://www.myfxbook.com/members/CyberPunkTrade/rockerboy-roboforex-copyfx-mt5-ecn/10955135', 'https://www.myfxbook.com/%22/members/finanzafree/%22', 'https://www.myfxbook.com/%22/members/Chibuike01/%22', 'https://www.myfxbook.com/members/Fernando01/rodrigo437/8692427', 'https://www.myfxbook.com/members/roegy/roegy/7648261', 'https://www.myfxbook.com/members/0220Rogel/rpm-cx-prima-ea/10488950', 'https://www.myfxbook.com/members/Surawinata29/rudi-supriadi-surawinata/11063818', 'https://www.myfxbook.com/members/R_Master/r-master-fusion-scalper-big/10899548', 'https://www.myfxbook.com/members/hothianmin/s9-gold-x35/10772498', 'https://www.myfxbook.com/members/investingpartner/safemove01/5237622', 'https://www.myfxbook.com/members/kamce93/sagar/9252660', 'https://www.myfxbook.com/members/NazhimNazri/salute/9437505', 'https://www.myfxbook.com/members/r4ibOm/samurai-swing-trading/11058763', 'https://www.myfxbook.com/members/samuraiea119/samurai3566/8247684', 'https://www.myfxbook.com/members/KIN_FX/samuraipro-insta-rub/11034551', 'https://www.myfxbook.com/members/Sammulchan96/sc-capital-management/9024740', 'https://www.myfxbook.com/members/iminwarn/scalper/9306398', 'https://www.myfxbook.com/members/brunol7/scalper-standard/10941691', 'https://www.myfxbook.com/members/Pikasso/scr-euraud/3099604', 'https://www.myfxbook.com/members/SGMMFX/sgmmfx-master-account-season-1/11081902', 'https://www.myfxbook.com/members/Rodrixxx/shredder-bot/9747323', 'https://www.myfxbook.com/members/Godfx007/sir-siba/9879346', 'https://www.myfxbook.com/members/fxknot/sleepsheep/6891995', 'https://www.myfxbook.com/members/Chuksheroic/smart-forex-ai-b2/9925280', 'https://www.myfxbook.com/members/Chuksheroic/smart-forex-al-b2/9875305', 'https://www.myfxbook.com/members/alanmhd7/smartfx-grid/10054922', 'https://www.myfxbook.com/members/smartforexrobots/smfx-scalper-pro-28/10902451', 'https://www.myfxbook.com/members/cakesniper/sniper-103/9170128', 'https://www.myfxbook.com/members/deenwildanfx/snmtc/9445914', 'https://www.myfxbook.com/members/Xyming/snowball-50/10115521', 'https://www.myfxbook.com/members/Xyming/snowball-50-tickmill/10116452', 'https://www.myfxbook.com/members/griosm/socialtradesignals/5781858', 'https://www.myfxbook.com/members/kris1002/sputnik2019/11155388', 'https://www.myfxbook.com/members/supcnr/sqs/7914798', 'https://www.myfxbook.com/members/ch4pom3keu21/st1853/10208165', 'https://www.myfxbook.com/members/ch4pom3keu21/st1926/10208139', 'https://www.myfxbook.com/members/reateaerey/st666/9143755', 'https://www.myfxbook.com/members/community_first/standard-cent-poonim/6268148', 'https://www.myfxbook.com/members/Meltory/star-light/10613726', 'https://www.myfxbook.com/members/StarGoGo/stargogo/2517413', 'https://www.myfxbook.com/members/Ara_2000/stochbol-5-1-gold/7058259', 'https://www.myfxbook.com/members/FxGpict/stock-robofx-ecn-mt5/9170548', 'https://www.myfxbook.com/members/Stormers96/stormbreaker/8847129', 'https://www.myfxbook.com/members/saroq61/stray-dog-account-1/4476953', 'https://www.myfxbook.com/members/saroq61/stray-dog-account-2/4750233', 'https://www.myfxbook.com/members/suchl/su01/2413532', 'https://www.myfxbook.com/members/sugiliang/sugi/7441085', 'https://www.myfxbook.com/%22/members/SnowWhalle/%22', 'https://www.myfxbook.com/members/pengxianyao/svxstr-v41-live-2021/7603099', 'https://www.myfxbook.com/members/free20190720/systema/9414639', 'https://www.myfxbook.com/members/murauchi_0605/systema1945/9152820', 'https://www.myfxbook.com/members/kamata_0626_2019/systemb1995/9152880', 'https://www.myfxbook.com/members/Tarkleads/t1000/9908748', 'https://www.myfxbook.com/members/Tarkleads/t2000/9912170', 'https://www.myfxbook.com/members/Tarkleads/t500/9912134', 'https://www.myfxbook.com/members/taichi20200218/taichi20200218/4706567', 'https://www.myfxbook.com/members/jovasu/terminator-3/10979030', 'https://www.myfxbook.com/members/Bentmariner/thunder-blue/10857777', 'https://www.myfxbook.com/members/hegemony88/tianhe-th/9628170', 'https://www.myfxbook.com/members/0stapBender/tio-billions/7672401', 'https://www.myfxbook.com/members/TirthasMoney/tirthas-asset/9964489', 'https://www.myfxbook.com/members/Nexwell/titan-gbpcad/7450843', 'https://www.myfxbook.com/members/SwapsRollovers/titanfx-news-tradingrisk-events/11018475', 'https://www.myfxbook.com/members/MTsinogi/tono7271/9143360', 'https://www.myfxbook.com/members/fonziefx/topgun-xversion/10982714', 'https://www.myfxbook.com/members/VEERAPHAT/trade-eu/8735328', 'https://www.myfxbook.com/members/TradeWithaT/tradet-controlled-grid/10606910', 'https://www.myfxbook.com/members/Tradehunters/tradehunters/11047921', 'https://www.myfxbook.com/members/gcotm/traderx-25k/10873893', 'https://www.myfxbook.com/members/FCAcademyTS/trading-hero/8442291', 'https://www.myfxbook.com/members/Trad1ngHero/trading-hero-100-000/10568480', 'https://www.myfxbook.com/members/Trad1ngHero/trading-hero-50-000/10568499', 'https://www.myfxbook.com/members/FCAcademyTS/trading-hero-5k/10330743', 'https://www.myfxbook.com/members/tradingsvietnam/tradings-capital/7232342', 'https://www.myfxbook.com/members/ArcLab/trail-magic/9098107', 'https://www.myfxbook.com/members/Upavla/trd-non-stop/4195609', 'https://www.myfxbook.com/members/sqyong/tsf-m15-eu-ex-ptau/7612473', 'https://www.myfxbook.com/members/aarontdang/tt1/4312047', 'https://www.myfxbook.com/members/Kirillza/turbo-mining/10652699', 'https://www.myfxbook.com/members/MariSus/turbo200/7599553', 'https://www.myfxbook.com/members/Ludopatico/turtle-safe/6969786', 'https://www.myfxbook.com/members/UCapital24/ucapital-usdjpy-sr-breakout/9742201', 'https://www.myfxbook.com/members/rumax1704/ultra-30/3160717', 'https://www.myfxbook.com/members/ar2rka/unstoppable/8920167', 'https://www.myfxbook.com/members/tec_daniel/uphill-mt5/10225619', 'https://www.myfxbook.com/members/yoni016/upmath/10609992', 'https://www.myfxbook.com/members/eagle70/v1s-tfi-token-bep20-vers/9333586', 'https://www.myfxbook.com/members/zeeee/v3cp-cents/9524452', 'https://www.myfxbook.com/members/vertexacdmy/vertex-nooknik-smc-technical/10817313', 'https://www.myfxbook.com/members/VBellon/v%C3%ADctorbell%C3%B3n/3248141', 'https://www.myfxbook.com/members/VincTamayao/vincent-paul-tamayao/8994934', 'https://www.myfxbook.com/members/gepards/virtual-ave-12-ea-mix/7589744', 'https://www.myfxbook.com/members/SwingFish/vixer/6293537', 'https://www.myfxbook.com/members/VOSYNHAT/vo-sy-nhat/9138891', 'https://www.myfxbook.com/%22/members/fbritop/%22', 'https://www.myfxbook.com/members/Wadjed/wavevol/8730170', 'https://www.myfxbook.com/%22/members/LifeisGood365/%22', 'https://www.myfxbook.com/members/yoyochrist/wijaya-moderate-fund-7758/9393489', 'https://www.myfxbook.com/members/WolvesVN/wolvesvn-cent-mao-hiem/11145429', 'https://www.myfxbook.com/members/wylielee/woodpeckers/7642509', 'https://www.myfxbook.com/members/feodor79/wsb-finex/4718355', 'https://www.myfxbook.com/members/anggaditastudio/x-series/8731697', 'https://www.myfxbook.com/members/andriosuroyo/xauusd-mixed/8865516', 'https://www.myfxbook.com/members/YUWENXIN/xinance-tw/8782015', 'https://www.myfxbook.com/members/OgidaniLLC/xm-real-mt5/9639750', 
# 'https://www.myfxbook.com/members/thanawat6454/xm-swap-free/9154812', 'https://www.myfxbook.com/members/Susanto_Adhi/xm-hrdc/9435251', 'https://www.myfxbook.com/members/sutiwat/xm-zenki/8739473', 'https://www.myfxbook.com/members/zaniah/xtb-real/3221378', 'https://www.myfxbook.com/members/yamahideyuu/ygold/11046029', 'https://www.myfxbook.com/members/yashin76/ysn-capital-group-icmarkets-serie/10493586', 'https://www.myfxbook.com/%22/members/zgrini21/%22', 'https://www.myfxbook.com/members/jsripien/zojen/10898439', 'https://www.myfxbook.com/members/eakboyza/zulukingeabolin/7591145', 'https://www.myfxbook.com/members/ZveroBot/zverobot-medium/7587550', 'https://www.myfxbook.com/members/buyvol/%D0%B0%D1%82%D0%BE%D0%BC/8734874', 'https://www.myfxbook.com/members/Giurza/%D0%BE%D1%81%D0%BD%D0%BE%D0%B2%D0%B0/7964358', 'https://www.myfxbook.com/members/tvi86/%D0%BE%D1%82-%D1%84%D0%BE%D0%BD%D0%B0%D1%80%D1%8F-%D1%83%D1%80%D0%BE%D0%B2%D0%BD%D0%B5%D0%B9/1263615', 'https://www.myfxbook.com/members/indyxa/%E0%B8%95%E0%B8%B2%E0%B8%A2%E0%B9%80%E0%B8%9E%E0%B8%A3%E0%B8%B2%E0%B8%B0%E0%B9%80%E0%B8%A5%E0%B8%99-abc-%E0%B9%84%E0%B8%A1%E0%B8%8A%E0%B8%94%E0%B9%80%E0%B8%88%E0%B8%99/8345832', 'https://www.myfxbook.com/members/Dampel/eternity/9171857', 'https://www.myfxbook.com/members/xRomanticEAx/mt4romanticccb-short/10629199', 'https://www.myfxbook.com/members/xRomanticEAx/mt4romanticccb-ver2/10629216', 'https://www.myfxbook.com/members/qazxcv1/%E3%83%89%E3%83%AB%E3%83%8F%E3%83%B3%E3%82%BF%E3%83%BC/8690308', 'https://www.myfxbook.com/members/sengoku/%E6%A5%B5gold%E6%94%B9%E9%80%86%E8%A5%B215%E5%88%86%E8%B6%B3%E8%A4%87%E5%88%A9100xs%E3%83%AA%E3%82%A2%E3%83%AB/10684734']

link_for_scrape = [
    # 'https://www.myfxbook.com/members/3ton_io/3ton-enhanced-alpha-30/9726950',
    # 'https://www.myfxbook.com/members/vshmonov/4-profit-fx321/3615560',
    'https://www.myfxbook.com/members/vshmonov/3-profit-fx321/3617787',
    # 'https://www.myfxbook.com/members/kyuirori/oldhearth-ea02-2/9374810'
    ]

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
def initialize_driver():
    """Initialize WebDriver with options."""
    options = Options()
    # options.add_argument("--headless")  # Run in headless mode
    # options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920x1080")
    return webdriver.Chrome(options=options)

def login_to_myfxbook(driver, username, password):
    """Login to Myfxbook."""
    driver.get("https://www.myfxbook.com/login")
    time.sleep(5)
    # Perform login
    driver.find_element(By.ID, "loginEmail").send_keys(username)
    driver.find_element(By.ID, "loginPassword").send_keys(password)
    driver.find_element(By.ID, "login-btn").click()
    time.sleep(5)
    logging.info("Logged into Myfxbook.")
    time.sleep(5)

def handle_popup(driver):
    """Handle any popup modals."""
    try:
        modal = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "popupAdModal"))
        )
        modal.find_element(By.XPATH, '//button[@data-dismiss="modal"]').click()
        logging.info("Popup handled.")
    except Exception:
        logging.info("No popup appeared.")

def scrape_watched_links(driver):
    """Scrape links from the Watched list."""
    # Click the "Watched" toggle to make the list visible
    try:
        watched_tab = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.ID, "watchedTab"))
        )
        watched_tab.click()
        print("Clicked on the 'Watched' tab.")
        time.sleep(3)  # Allow time for the table to load
    except Exception as e:
        print(f"Error clicking on 'Watched' tab: {e}")
        driver.quit()
        exit()

    # Wait for the watched table to load
    try:
        watched_table = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "watchedTable"))
        )
        print("Watched table loaded.")
    except Exception as e:
        print("Error loading watched table:", e)
        driver.quit()
        exit()

    # Locate the "watchedTable" and extract system links
    rows = watched_table.find_elements(By.XPATH, '//tr[contains(@class, "watchedAccountRow")]')

    system_links = []
    for row in rows:
        try:
            link_element = row.find_element(By.TAG_NAME, "a")
            system_links.append(link_element.get_attribute("href"))
        except Exception as e:
            print(f"Error extracting link from row: {e}")

    if system_links:
        print(f"Found {len(system_links)} system links.")
    else:
        print("No system links found.")
        driver.quit()
        exit()
    return system_links

def scrape_section_data(driver, section_id):
    print("Scrape Section data runs")
    """Scrape data from a specific section by its ID."""
    data = {}
    if section_id == 'infoGeneral':
        try:
            # Locate and click the tab, ensuring it's clickable
            watched_tab = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.ID, "infoGeneralTab"))
            )
            # Scroll the element into view to avoid interception
            driver.execute_script("arguments[0].scrollIntoView(true);", watched_tab)
            # Use JavaScript to click if direct click fails
            driver.execute_script("arguments[0].click();", watched_tab)
            print("Clicked on the 'infoGeneralTab' tab successfully.")
            time.sleep(3)  # Allow time for the table to load
        except Exception as e:
            print(f"Error clicking on 'infoGeneralTab' tab: {e}")
            # Optional: Save a screenshot for debugging
            # driver.save_screenshot("infoGeneralTab_click_error.png")
            return {}
        section_container = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.ID, "system-info-section"))
        )
        # Locate and click the tab, ensuring it's clickable
        tables = section_container.find_elements(By.CSS_SELECTOR, "table")
        for table in tables:
            rows = table.find_elements(By.TAG_NAME, "tr")
            for row in rows:
                cells = row.find_elements(By.TAG_NAME, "td")
                if len(cells) == 2:
                    key = cells[0].text.strip()
                    value = cells[1].text.strip()
                    print("KEY: ", key, "Value: ", value)
                    data[key] = value
                    if key == 'Started:':
                        started_date = value
                        print("Started key is: ", value)
                        # try:
                        started_datetime = datetime.strptime(started_date, "%b %d, %Y")
                        cutoff_datetime = datetime(2019, 12, 31)
                        if started_datetime > cutoff_datetime:
                            print(f"'Started' date {started_date} is later than December 2019. Skipping link.")
                            return None,None
                        else:
                            history_data = scrape_history_trade_data(driver)
                        # except ValueError:
                        #     print(f"Invalid date format for 'Started': {started_date}. Skipping link.")
                        #     return None

    return data, history_data  # Return both general data and history data

# def scrape_history_trade_data(driver):
#     data = {}
#     print("Scrape History Trade data runs")
#     try:
#         # Wait for the History tab to become clickable
#         history_tab = WebDriverWait(driver, 20).until(
#             EC.element_to_be_clickable((By.ID, "tabHistory"))
#         )
        
#         # Scroll the element into view to avoid interception
#         driver.execute_script("arguments[0].scrollIntoView(true);", history_tab)
        
#         # Click the <a> tag inside the <li> with ID 'tabHistory'
#         history_link = history_tab.find_element(By.TAG_NAME, "a")
#         driver.execute_script("arguments[0].click();", history_link)
        
#         print("Clicked on the 'tabHistory' tab successfully.")
#         time.sleep(3)  # Allow time for the table to load
#     except Exception as e:
#         print(f"Error clicking on 'tabHistory' tab: {e}")
#         return {}

#     return data
  
# def scrape_history_trade_data(driver):
#     data = {}
#     print("Scrape History Trade data runs")
#     date_format = "%m.%d.%Y %H:%M"  # Expected date format in the table
#     start_date = datetime.strptime("12.01.2019 00:00", date_format)
#     end_date = datetime.strptime("04.30.2020 23:59", date_format)
#     try:
#         # Wait for the History tab to become clickable
#         history_tab = WebDriverWait(driver, 20).until(
#             EC.element_to_be_clickable((By.ID, "tabHistory"))
#         )
        
#         # Scroll the element into view to avoid interception
#         driver.execute_script("arguments[0].scrollIntoView(true);", history_tab)
        
#         # Click the <a> tag inside the <li> with ID 'tabHistory'
#         history_link = history_tab.find_element(By.TAG_NAME, "a")
#         driver.execute_script("arguments[0].click();", history_link)
        
#         print("Clicked on the 'tabHistory' tab successfully.")
#         time.sleep(3)  # Allow time for the table to load
#     except Exception as e:
#         print(f"Error clicking on 'tabHistory' tab: {e}")
#         return {}
    
#     # Function to parse date strings into datetime objects
#     def parse_date(date_string):
#         try:
#             return datetime.strptime(date_string, date_format)
#         except ValueError:
#             print(f"Invalid date format: {date_string}")
#             return None  # Handle empty or invalid date fields
        
#     # try:
#     while True:
#         # Locate the table in the History section
#         history_table = WebDriverWait(driver, 20).until(
#             EC.presence_of_element_located((By.CSS_SELECTOR, "table#tradingHistoryTable"))
#         )

#         # Extract headers from the table
#         headers = [
#             header.text.strip()
#             for header in history_table.find_elements(By.CSS_SELECTOR, "thead tr th")
#         ]
#         print(f"Extracted headers: {headers}")

#         # Extract rows from the table
#         rows = history_table.find_elements(By.CSS_SELECTOR, "tbody tr")
#         for index, row in enumerate(rows, start=1):
#             cells = row.find_elements(By.TAG_NAME, "td")
#             row_data = [cell.text.strip() for cell in cells]
#             # Extract Open Date and filter by range
#             open_date = parse_date(row_data[1])  # Assuming 'Open Date' is the first column
#             print("Open Date: ", open_date)
#             if open_date and start_date <= open_date <= end_date:
#                 data[f"Row_{len(data) + 1}"] = dict(zip(headers, row_data))
#             elif open_date and open_date > end_date:
#                 # If the Open Date is beyond the desired range, stop processing further
#                 print("Open Date is beyond the desired range. Stopping pagination.")
#                 try:
#                     pagination = driver.find_element(By.CSS_SELECTOR, "#historyCont .pagination")
#                     # Locate the "Next" button
#                     next_button = WebDriverWait(driver, 10).until(
#                         EC.presence_of_element_located((By.CSS_SELECTOR, "#historyCont .pagination li.next a"))
#                     )
#                     if "disabled" in next_button.get_attribute("class"):
#                         print("No more pages available.")
#                         break  # Stop if the next button is disabled

#                     driver.execute_script("arguments[0].click();", next_button)
#                     print("Navigated to the next page.")
#                     time.sleep(2)

#                 except Exception as pagination_error:
#                     print(f"No further pages available or error in pagination: {pagination_error}")
#                     break
#                 # return data
#             print(f"Row {index}: {row_data}")

#                 # Map row data to corresponding headers
#                 # data[f"Row_{index}"] = dict(zip(headers, row_data))
#             # Navigate to the next page if available
#             # try:
#             #     pagination = driver.find_element(By.CSS_SELECTOR, "#historyCont .pagination")
#             #     next_button = pagination.find_element(By.CSS_SELECTOR, "li.next")

#             #     if "disabled" in next_button.get_attribute("class"):
#             #         print("No more pages available.")
#             #         break  # Stop if the next button is disabled

#             #     driver.execute_script("arguments[0].click();", next_button)
#             #     print("Navigated to the next page.")
#             #     time.sleep(2)

#             # except Exception as pagination_error:
#             #     print(f"No further pages available or error in pagination: {pagination_error}")
#             #     break

#             # print("History trade data successfully scraped.")
#     # except Exception as e:
#     #     print(f"Error extracting data from the History table: {e}")
#     #     return {}

#     return data
  
# def scrape_history_trade_data(driver):
#     data = {}
#     print("Scrape History Trade data runs")
#     date_format = "%m.%d.%Y %H:%M"  # Expected date format in the table
#     start_date = datetime.strptime("12.01.2019 00:00", date_format)
#     end_date = datetime.strptime("04.30.2020 23:59", date_format)

#     try:
#         # Wait for the History tab to become clickable
#         history_tab = WebDriverWait(driver, 20).until(
#             EC.element_to_be_clickable((By.ID, "tabHistory"))
#         )
#         driver.execute_script("arguments[0].scrollIntoView(true);", history_tab)
#         driver.execute_script("arguments[0].click();", history_tab.find_element(By.TAG_NAME, "a"))
#         print("Clicked on the 'tabHistory' tab successfully.")
#         time.sleep(3)  # Allow time for the table to load
#     except Exception as e:
#         print(f"Error clicking on 'tabHistory' tab: {e}")
#         return {}

#     def parse_date(date_string):
#         try:
#             return datetime.strptime(date_string, date_format)
#         except ValueError:
#             print(f"Invalid date format: {date_string}")
#             return None

#     while True:
#         try:
#             # Locate the table on the current page
#             history_table = WebDriverWait(driver, 20).until(
#                 EC.presence_of_element_located((By.CSS_SELECTOR, "table#tradingHistoryTable"))
#             )

#             # Extract headers
#             headers = [
#                 header.text.strip()
#                 for header in history_table.find_elements(By.CSS_SELECTOR, "thead tr th")
#             ]
#             print(f"Extracted headers: {headers}")

#             # Extract rows
#             rows = history_table.find_elements(By.CSS_SELECTOR, "tbody tr")
#             for index, row in enumerate(rows, start=1):
#                 cells = row.find_elements(By.TAG_NAME, "td")
#                 row_data = [cell.text.strip() for cell in cells]

#                 open_date = parse_date(row_data[1])  # Assuming 'Open Date' is the second column
#                 print("Open Date: ", open_date)

#                 if open_date and start_date <= open_date <= end_date:
#                     data[f"Row_{len(data) + 1}"] = dict(zip(headers, row_data))
#                 elif open_date and open_date > end_date:
#                     print("Open Date is beyond the desired range. Stopping pagination.")
#                     break

#                 print(f"Row {index}: {row_data}")

#             # Navigate to the next page
#             try:
#                 next_button = WebDriverWait(driver, 10).until(
#                     EC.presence_of_element_located((By.CSS_SELECTOR, "#historyCont .pagination li.next a"))
#                 )
#                 if "disabled" in next_button.get_attribute("class"):
#                     print("No more pages available.")
#                     break
#                 driver.execute_script("arguments[0].click();", next_button)
#                 print("Navigated to the next page.")
#                 time.sleep(3)
#             except Exception as pagination_error:
#                 print(f"No further pages available or error in pagination: {pagination_error}")
#                 break

#         except Exception as e:
#             print(f"Error while processing the History table: {e}")
#             break

#     return data

def scrape_history_trade_data(driver):
    print("Scrape History Trade data runs")
    data = {}
    date_format = "%m.%d.%Y %H:%M"
    # start_date = datetime.strptime("12.01.2019 00:00", date_format)
    # end_date = datetime.strptime("04.30.2020 23:59", date_format)
    start_date = datetime.strptime("02.27.2022 00:00", date_format)
    end_date = datetime.strptime("10.8.2021 23:59", date_format)

    # Navigate to History tab
    try:
        # Navigate to the History tab
        history_tab = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.ID, "tabHistory"))
        )
        driver.execute_script("arguments[0].scrollIntoView(true);", history_tab)
        driver.execute_script("arguments[0].click();", history_tab.find_element(By.TAG_NAME, "a"))
        print("Clicked on the 'tabHistory' tab successfully.")
        time.sleep(5)
    except Exception as e:
        print(f"Error clicking on 'tabHistory' tab: {e}")
        return {}

    def parse_date(date_string):
        try:
            return datetime.strptime(date_string, date_format)
        except ValueError:
            print(f"Invalid date format: {date_string}")
            return None

    while True:
        try:
            # Locate the table on the current page
            history_table = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "table#tradingHistoryTable"))
            )

            # Extract headers
            headers = [
                header.text.strip()
                for header in history_table.find_elements(By.CSS_SELECTOR, "thead tr th")
            ]
            print(f"Extracted headers: {headers}")

            filtered_headers = [h for h in headers if h]  # Remove empty headers
            print(f"Filtered Headers: {filtered_headers}")

            # Extract rows
            rows = history_table.find_elements(By.CSS_SELECTOR, "tbody tr")
            for index, row in enumerate(rows, start=1):
                cells = row.find_elements(By.TAG_NAME, "td")
                row_data = [cell.text.strip() for cell in cells]

                # Remove empty values in the row corresponding to removed headers
                filtered_row_data = {k: v for k, v in row.items() if v}

                # Map filtered headers to filtered row data
                row_dict = dict(zip(filtered_headers, filtered_row_data))

                open_date = parse_date(row_dict.get("Open Date"))  # Fetch Open Date safely
                print("Open Date: ", open_date)

                if open_date:
                    if open_date > start_date:
                        print(f"🚀 Skipping future date: {open_date}")
                        continue
                    elif open_date < end_date:
                        print(f"🔴 Open Date {open_date} is beyond the desired range. Stopping pagination.")
                        print("📌 Data collected so far:", data)
                        return data  # Stop execution

                    data[f"Row_{len(data) + 1}"] = row_dict

                print(f"✅ Row {index}: {row_data}")

            # Navigate to the next page
            try:
                next_button = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, "#historyCont .pagination li.next a"))
                )
                if "disabled" in next_button.get_attribute("class"):
                    print("No more pages available.")
                    break
                driver.execute_script("arguments[0].click();", next_button)
                print("Navigated to the next page.")
                time.sleep(3)
            except Exception as pagination_error:
                print(f"No further pages available or error in pagination: {pagination_error}")
                break

        except Exception as e:
            print(f"Error while processing the History table: {e}")
            break

    return data

# Modified scrape_system_data to integrate saving
def scrape_system_data(driver, link):
    """Scrape data from a specific system link and save to Excel"""
    system_data = {
        "system": {},
        "infoGeneral": {},
        "history": {}  # This will be populated by scrape_history_trade_data
    }
    
    try:
        driver.get(link)
        time.sleep(2)

        # Get system name
        system_name = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.TAG_NAME, "h1"))
        ).text.strip()
        system_data["system"]["system"] = system_name

        # Get general info and history data from scrape_section_data
        general_data, history_data = scrape_section_data(driver, "infoGeneral")

        if general_data is None:
            print("Skipping system due to invalid start date.")
            return None

        system_data["infoGeneral"] = general_data
        system_data["history"] = history_data  # This now contains the history data

        # Save to Excel
        save_to_excel(system_data)
        return system_data

    except Exception as e:
        print(f"Error in processing system: {e}")
        return None

PREDEFINED_HEADERS = [
    'method', 'trading', 'system', 'Open Date', 'Close date', 'Symbol',
    'Action', 'Open Price', 'Close Price', 'Profit (USD)', 'Duration', 'Gain']

def save_to_excel(data, filename="trading_data.xlsx"):
    """Save scraped data to Excel with predefined structure"""

    # Load existing data if file exists, otherwise create an empty DataFrame
    if os.path.exists(filename):
        df = pd.read_excel(filename)
    else:
        df = pd.DataFrame(columns=PREDEFINED_HEADERS)

    # Extract general info
    method = data.get('infoGeneral', {}).get('System', '')
    trading = data.get('infoGeneral', {}).get('Trading', '')
    system = data.get('system', {}).get('system', '')

    # Extract history data (Iterate over multiple rows)
    history_data = data.get('history', {})
    new_rows = []
    
    for row_key, row in history_data.items():
        # Prepare row data
        row_data = {
            'method': method,
            'trading': trading,
            'system': system,
            'Open Date': row.get('Open Date', ''),
            'Close date': row.get('Close date', ''),
            'Symbol': row.get('Symbol', ''),
            'Action': row.get('Action', ''),
            'Open Price': row.get('Open Price', ''),
            'Close Price': row.get('Close Price', ''),
            'Profit (USD)': row.get('Profit\n(USD)', ''),  # Fixing key mismatch
            'Duration': row.get('Duration', ''),
            'Gain': row.get('Gain', '')
        }

        # Convert date strings to datetime objects
        date_columns = ['Open Date', 'Close date']
        for col in date_columns:
            if row_data[col]:
                try:
                    row_data[col] = datetime.strptime(row_data[col], "%m.%d.%Y %H:%M")
                except ValueError:
                    row_data[col] = None  # Invalid date format handling

        new_rows.append(row_data)

    # Create DataFrame for new rows
    new_df = pd.DataFrame(new_rows)

    # Append to existing data
    df = pd.concat([df, new_df], ignore_index=True)

    # Save to Excel
    try:
        df.to_excel(filename, index=False)
        print(f"Data successfully saved to {filename}")
        return True
    except Exception as e:
        print(f"Error saving to Excel: {e}")
        return False
    
if __name__ == "__main__":
    username = "evan.mlburgess@gmail.com"
    password = "Qwertyuiop1!"
    
    driver = initialize_driver()
    try:
        # login_to_myfxbook(driver, username, password)
        # handle_popup(driver)
        # system_links = scrape_watched_links(driver)
        
        # print("System links: ",system_links)
        
        # Get the list of already-scraped system names
        # existing_system_names = get_existing_system_names()

        if link_for_scrape:
            start_index = 626  # Starting index for slicing
            end_index = 672    # Ending index for slicing
            for link in link_for_scrape:
                # print(f"Processing link {i}: {link}")
                print("Current link: ", link)
                
                # Navigate to the link to get the system name first
                driver.get(link)
                time.sleep(2)  # Adjust based on page load speed

                try:
                    # Retrieve the system name
                    system_name = WebDriverWait(driver, 20).until(
                        EC.presence_of_element_located((By.TAG_NAME, "h1"))  # Replace with actual selector
                    ).text.strip()
                    
                    # if system_name in existing_system_names:
                    #     print(f"System '{system_name}' already exists. Skipping...")
                    #     continue  # Skip this link if the system name is already in the file
                    
                    # If not already processed, scrape the system data
                    data = scrape_system_data(driver, link)
                    # if data:
                    #     save_to_excel_single(data)  # Save the scraped data immediately
                        # Add the system name to the set to avoid reprocessing in the same run
                        # existing_system_names.add(system_name)
                except TimeoutException:
                    logging.error(f"Timeout while accessing link: {link}. Skipping this link.")
                except Exception as e:
                    logging.error(f"Unexpected error while processing link: {link}. Error: {e}")
        else:
            logging.info("No system links to scrape.")
    finally:
        driver.quit()
        logging.info("Browser closed.")

 