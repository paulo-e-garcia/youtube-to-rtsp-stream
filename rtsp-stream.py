import subprocess
import sys
import time

def get_youtube_stream_url(youtube_url):
    try:
        result = subprocess.run(
            ['yt-dlp', '-f', 'best', '-g', youtube_url],
            capture_output=True,
            text=True,
            check=True
        )
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print(f"Erro ao obter URL do Youtube.: {e}")
        sys.exit(1)

def start_mediamtx():
    try:
        subprocess.run(['pgrep', '-x', 'mediamtx'], 
                      capture_output=True, check=True)
        print("MediaMTX já está rodando.")
        return None
    except subprocess.CalledProcessError:
        print("Iniciando MediaMTX...")
        proc = subprocess.Popen(['mediamtx'], 
                               stdout=subprocess.DEVNULL,
                               stderr=subprocess.DEVNULL)
        time.sleep(2) # tempo para o servidor subir
        return proc

def stream_to_rtsp(stream_url, rtsp_output):
    """Usa FFmpeg para gerar stream do vídeo no protocolo RTSP"""
    cmd = [
        'ffmpeg',
        '-i', stream_url,
        '-c:v', 'copy',
        '-c:a', 'aac',
        '-ar', '44100',
        '-f', 'rtsp',
        rtsp_output
    ]
    
    print(f"Iniciando stream no endereço {rtsp_output}...")
    try:
        subprocess.run(cmd, check=True)
    except KeyboardInterrupt:
        print("\nStream cancelado.")
    except subprocess.CalledProcessError as e:
        print(f"Erro FFmpeg: {e}")
        sys.exit(1)

def main():
    youtube_url = "https://www.youtube.com/watch?v=3LXQWU67Ufk" # Substitua "v=xxxxx" pelo código no final da URL do video no Youtube
    rtsp_output = "rtsp://localhost:8554/mystream" # Altere conforme a necessidade
    
    # Inicia MediaMTX
    mediamtx_proc = start_mediamtx()
    
    try:
        # Tenta obter a URL do Youtube. Dando certo, inicia o stream no endereço RTSP provido acima.
        print(f"Obtendo URL do Youtube... {youtube_url}...")
        stream_url = get_youtube_stream_url(youtube_url)
        print(f"URL obtida com sucesso.")
        
        # Inicia Stream
        stream_to_rtsp(stream_url, rtsp_output)
        
    finally:
        # Desligamento do MediaMTX
        if mediamtx_proc:
            print("Parando MediaMTX...")
            mediamtx_proc.terminate()
            mediamtx_proc.wait()

if __name__ == "__main__":
    main()
