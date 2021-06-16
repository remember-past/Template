folder = data_folder

experiment = []
fid = open(folder+os.sep+r'genomic-scale.tsv','r')
lines = np.array([ln[:-1].split('\t')for ln in fid if len(ln)>0])
head = list(lines[0])
experiment = np.concatenate([experiment,lines[1::2082,head.index('experiment number')].astype(int)])
zxy = np.array(lines[1:,:3][:],dtype=np.float)
dLAM = np.array(lines[1:,-1].astype(float))

fid = open(folder+os.sep+r'genomic-scale-with transcription and nuclear bodies.tsv','r')
lines = np.array([ln[:-1].split('\t')for ln in fid if len(ln)>0])
head = list(lines[0])
experiment = np.concatenate([experiment,lines[1::2082,head.index('experiment number')].astype(int)])
dLAM = np.concatenate([dLAM,np.array(lines[1:,-3].astype(float))])
zxy = np.concatenate([zxy,np.array(lines[1:,:3][:],dtype=np.float)])
zxy = zxy.reshape([-1,2082,3])/1000 #transform to um
dLAM = dLAM.reshape([-1,2082])/1000