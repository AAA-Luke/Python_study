import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import mne
raw=mne.io.read_raw_gdf(r"E:\Study\BCI_Competition_Data\BCICIV_2a\A01T.gdf",preload=True)
print("======脑电数据基本信息=====")
print(raw.info)
print("采样率:",raw.info['sfreq'])
print("通道数量:",raw.info['nchan'])
events,event_id=mne.events_from_annotations(raw)
print("\n======事件ID对应关系=====")
print(event_id)
print("\n前十五个事件（采样点，0，事件编号）：")
print(events[:15])
fig=raw.plot(duration=5
             ,start=0,
             n_channels=10,
             scalings='auto')
plt.show(block=True)
raw.filter(l_freq=0.5,h_freq=30.0,verbose=True)
raw.notch_filter(freqs=50.0,verbose=True)
event_id={
    'left_hand':6,
    'right_hand':7
}
tmin,tmax=-0.2,3.0
epochs=mne.Epochs(
    raw,events,event_id=event_id,
    tmin=tmin,tmax=tmax,
    baseline=(None,0),preload=True
)
print("\n====截取的样本信息====")
print(epochs)
print("左手样本数量：",len(epochs['left_hand']))
print("右手样本数量：",len(epochs['right_hand']))