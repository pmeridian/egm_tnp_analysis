from libPython.tnpClassUtils import tnpSample

### qll stat
#eosDir1 = 'eos/cms/store/group/phys_egamma/tnp/80X/PhoEleIDs/v1/'
#eosDir2 = 'eos/cms/store/group/phys_egamma/tnp/80X/PhoEleIDs/v2/'
#eosDirREC = 'eos/cms/store/group/phys_egamma/tnp/80X/RecoSF/RECOSFs_2016/'
#eosWinter17 = 'eos/cms/store/group/phys_egamma/tnp/80X/PhoEleIDs/Moriond17_v1/'
#eosMoriond18 = '/eos/cms/store/group/phys_egamma/soffi/TnP/ntuples_01292018/Moriond18_V1/'
#eos2018Data_102X = '/eos/cms/store/group/phys_egamma/soffi/TnP/ntuples_20180920/2018Data_1/'

eosMoriond17 = '/eos/cms/store/group/phys_egamma/micheli/TnP/ntuples_2017_20181116/v1/'
eos2017Data_102X = '/eos/cms/store/group/phys_egamma/micheli/TnP/ntuples_2017_20181116/v1/'


Data2017_102X = {
    ### MiniAOD TnP for IDs scale 
    'DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8' : tnpSample('DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8', 
                                       eos2017Data_102X + 'mc/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8.root',
                                       isMC = True, nEvts =  -1 ),


    'data_Run2017B' : tnpSample('data_Run2017' , eos2017Data_102X + 'data/SingleEle2017B.root' , lumi = 42.6 ),
    'data_Run2017C' : tnpSample('data_Run2017' , eos2017Data_102X + 'data/SingleEle2017C.root' , lumi = 42.6 ),
    'data_Run2017D' : tnpSample('data_Run2017' , eos2017Data_102X + 'data/SingleEle2017D.root' , lumi = 42.6 ),
    'data_Run2017E' : tnpSample('data_Run2017' , eos2017Data_102X + 'data/SingleEle2017E.root' , lumi = 42.6 ),
    'data_Run2017F' : tnpSample('data_Run2017Dv2' , eos2017Data_102X + 'data/SingleEle2017F.root' , lumi = 42.6 ), 



    }



##about lumi: thse ntuples are done with /afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions18/13TeV/PromptReco/Cert_314472-321221_13TeV_PromptReco_Collisions18_JSON.txt = with recorded luminosity : 31.71 /fb but ~20% are crashed. Also we need to update the single runs lumi


 
