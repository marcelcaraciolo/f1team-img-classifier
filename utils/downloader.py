from bing_image_downloader import downloader

#for team in ['alphatauri', 'redbull', 'astonmartin', 'mclaren' , 'alpine', 'alfaromeo' , 'ferrari', 'williams', 'mercedes', 'haas']:
#    downloader.download(team + ' f1 2023 car', output_dir=team, limit=20, adult_filter_off=True, force_replace=False, timeout=60, verbose=True)


downloader.download("alphatauri f1 on track", output_dir="alphatauri", limit=25, adult_filter_off=True, force_replace=False, timeout=60, verbose=True)

