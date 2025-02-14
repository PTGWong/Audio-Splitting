import os
import librosa
import soundfile as sf

# 设置音频文件夹路径
audio_folder = 'YOU-PATH'  # 替换为你自己的文件夹路径
# audio_folder = 'path_to_audio_folder'  # 替换为你自己的文件夹路径

# 获取文件夹中所有音频文件
audio_files = [f for f in os.listdir(audio_folder) if f.endswith('.flac')]

# 遍历文件夹中的每个音频文件
for audio_file in audio_files:
    audio_path = os.path.join(audio_folder, audio_file)
    
    # 加载音频
    audio, sr = librosa.load(audio_path, sr=None)
    
    # 计算拆分点
    sixth_point = len(audio) // 6
    
    # 拆分音频成六部分
    audio_part1 = audio[:sixth_point]
    audio_part2 = audio[sixth_point:2*sixth_point]
    audio_part3 = audio[2*sixth_point:3*sixth_point]
    audio_part4 = audio[3*sixth_point:4*sixth_point]
    audio_part5 = audio[4*sixth_point:5*sixth_point]
    audio_part6 = audio[5*sixth_point:]
    
    # 保存拆分后的音频
    part1_path = os.path.join(audio_folder, f'{os.path.splitext(audio_file)[0]}_p1.flac')
    part2_path = os.path.join(audio_folder, f'{os.path.splitext(audio_file)[0]}_p2.flac')
    part3_path = os.path.join(audio_folder, f'{os.path.splitext(audio_file)[0]}_p3.flac')
    part4_path = os.path.join(audio_folder, f'{os.path.splitext(audio_file)[0]}_p4.flac')
    part5_path = os.path.join(audio_folder, f'{os.path.splitext(audio_file)[0]}_p5.flac')
    part6_path = os.path.join(audio_folder, f'{os.path.splitext(audio_file)[0]}_p6.flac')
    
    sf.write(part1_path, audio_part1, sr)
    sf.write(part2_path, audio_part2, sr)
    sf.write(part3_path, audio_part3, sr)
    sf.write(part4_path, audio_part4, sr)
    sf.write(part5_path, audio_part5, sr)
    sf.write(part6_path, audio_part6, sr)

    print(f'音频文件 {audio_file} 已拆分并保存为 {part1_path}、{part2_path}、{part3_path}、{part4_path}、{part5_path} 和 {part6_path}')