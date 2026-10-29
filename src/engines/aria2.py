import os
from src.core.logger import log

def download_torrent(target_url, download_dir, timeout_seconds=180):
    log("FETCH", "Kích hoạt engine aria2c P2P (DHT/Peer/Trackers)...", "FETCH")
    cmd = (
        f'aria2c --enable-dht=true --enable-dht6=true --bt-enable-lpd=true '
        f'--bt-max-peers=120 --seed-time=0 --bt-stop-timeout={timeout_seconds} '
        f'--summary-interval=10 --file-allocation=none -d "{download_dir}" "{target_url}"'
    )
    return os.system(cmd)

def download_direct(target_url, download_dir, connections=16):
    cmd = f'aria2c -x{connections} -s{connections} -k1M --file-allocation=none -d "{download_dir}" "{target_url}"'
    return os.system(cmd)
