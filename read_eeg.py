import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import mne
raw=mne.io.read_raw_gdf(r"E:\Study\BCI_Competition_Data\BCICIV_2a\A01T.gdf",preload=True)
print(raw.info)
fig=raw.plot(duration=5,n_channels=10)
plt.show(block=True)