#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ChHsich Nerd Font 创建脚本
将ComicShannsMono Nerd Font的特定字符替换到Maple Mono NF CN中
"""

import fontforge
import os
import glob
from pathlib import Path

def get_unicode_ranges():
    """返回需要替换的Unicode范围"""
    ranges = []
    
    # U+0021到U+007E (基本拉丁字母、数字和符号)
    ranges.append((0x0021, 0x007E))
    
    # 单个字符范围
    single_chars = [
        0x00A1, 0x00A2, 0x00A3, 0x00A4, 0x00A5, 0x00A6,  # U+00A1到U+00A6
        0x00AB,  # U+00AB
        0x00AC,  # U+00AC
        0x00AF,  # U+00AF
        0x00B0,  # U+00B0
        0x00B1,  # U+00B1
        0x00B4,  # U+00B4
        0x00BB,  # U+00BB
        0x00D7,  # U+00D7
        0x00F7   # U+00F7
    ]
    
    for char in single_chars:
        ranges.append((char, char))
    
    return ranges

def copy_glyphs_from_source_to_target(source_font, target_font, unicode_ranges):
    """从源字体复制指定Unicode范围的字符到目标字体"""
    print(f"开始复制字符...")
    
    copied_count = 0
    for start_unicode, end_unicode in unicode_ranges:
        for unicode_val in range(start_unicode, end_unicode + 1):
            try:
                if unicode_val in source_font:
                    char_name = source_font[unicode_val].glyphname
                    
                    # 检查目标字体是否已有该字符
                    if unicode_val in target_font:
                        print(f"替换字符 U+{unicode_val:04X} ({chr(unicode_val) if unicode_val < 0x10000 else '?'})")
                    else:
                        print(f"添加字符 U+{unicode_val:04X} ({chr(unicode_val) if unicode_val < 0x10000 else '?'})")
                    
                    # 从源字体复制字符
                    source_font.selection.select(unicode_val)
                    source_font.copy()
                    
                    # 如果目标字体已有该字符，先删除
                    if unicode_val in target_font:
                        target_font.selection.select(unicode_val)
                        target_font.clear()
                    
                    # 粘贴字符到目标字体
                    target_font.selection.select(unicode_val)
                    target_font.paste()
                    
                    copied_count += 1
                else:
                    print(f"警告: 源字体中未找到字符 U+{unicode_val:04X}")
            except Exception as e:
                print(f"错误: 处理字符 U+{unicode_val:04X} 时出错: {e}")
                continue
    
    print(f"字符复制完成，共复制了 {copied_count} 个字符")

def process_font_pair(comic_font_path, maple_font_path, output_path):
    """处理一对字体文件"""
    print(f"\n处理字体对:")
    print(f"源字体: {comic_font_path}")
    print(f"目标字体: {maple_font_path}")
    print(f"输出字体: {output_path}")
    
    # 打开字体
    comic_font = fontforge.open(comic_font_path)
    maple_font = fontforge.open(maple_font_path)
    
    # 获取需要替换的Unicode范围
    unicode_ranges = get_unicode_ranges()
    
    # 复制字符
    copy_glyphs_from_source_to_target(comic_font, maple_font, unicode_ranges)
    
    # 更新字体信息
    font_name = "ChHsich Nerd Font"
    maple_font.familyname = font_name
    maple_font.fontname = maple_font.fontname.replace("MapleMono-NF-CN", "ChHsichNerdFont")
    maple_font.fullname = maple_font.fullname.replace("Maple Mono NF CN", font_name)
    
    # 更新SFNT名称表
    print("更新SFNT名称表...")
    new_sfnt_names = []
    for name in maple_font.sfnt_names:
        lang, name_id, value = name
        
        # 更新Family名称
        if name_id == 'Family':
            new_value = font_name
        # 更新Fullname
        elif name_id == 'Fullname':
            new_value = value.replace("Maple Mono NF CN", font_name)
        # 更新PostScriptName
        elif name_id == 'PostScriptName':
            new_value = value.replace("MapleMono-NF-CN", "ChHsichNerdFont")
        # 更新UniqueID
        elif name_id == 'UniqueID':
            new_value = value.replace("MapleMono-NF-CN", "ChHsichNerdFont")
        # 更新Preferred Family
        elif name_id == 'Preferred Family':
            new_value = font_name
        # 更新Copyright（可选，如果你想完全移除Maple相关信息）
        elif name_id == 'Copyright':
            new_value = "Copyright 2024 ChHsiching (https://github.com/ChHsiching/chhsich-nerd-font). Based on ComicShannsMono Nerd Font."
        else:
            new_value = value
        
        new_sfnt_names.append((lang, name_id, new_value))
    
    # 应用新的SFNT名称
    maple_font.sfnt_names = new_sfnt_names
    
    # 确保输出目录存在
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    # 保存字体
    print(f"保存字体到: {output_path}")
    maple_font.generate(output_path)
    
    # 关闭字体
    comic_font.close()
    maple_font.close()
    
    print(f"完成: {output_path}")

def main():
    """主函数"""
    print("开始创建 ChHsich Nerd Font...")
    
    # 定义路径
    comic_dir = "ComicShannsMono"
    maple_dir = "MapleMono-NF-CN-unhinted"
    output_dir = "ChHsichNerdFont"
    
    # 获取ComicShannsMono字体文件
    comic_fonts = glob.glob(os.path.join(comic_dir, "*.otf"))
    if not comic_fonts:
        print(f"错误: 在 {comic_dir} 目录中未找到.otf字体文件")
        return
    
    # 获取MapleMono字体文件
    maple_fonts = glob.glob(os.path.join(maple_dir, "*.ttf"))
    if not maple_fonts:
        print(f"错误: 在 {maple_dir} 目录中未找到.ttf字体文件")
        return
    
    print(f"找到 {len(comic_fonts)} 个ComicShannsMono字体文件")
    print(f"找到 {len(maple_fonts)} 个MapleMono字体文件")
    
    # 处理每个字体对
    for maple_font_path in maple_fonts:
        # 获取字体名称
        maple_filename = os.path.basename(maple_font_path)
        maple_name = os.path.splitext(maple_filename)[0]
        
        # 确定对应的ComicShannsMono字体
        comic_font_path = None
        
        # 根据MapleMono字体名称匹配ComicShannsMono字体
        if "Bold" in maple_name and "Italic" in maple_name:
            comic_font_path = os.path.join(comic_dir, "ComicShannsMonoNerdFont-Bold.otf")
        elif "Bold" in maple_name:
            comic_font_path = os.path.join(comic_dir, "ComicShannsMonoNerdFont-Bold.otf")
        elif "Italic" in maple_name:
            comic_font_path = os.path.join(comic_dir, "ComicShannsMonoNerdFont-Regular.otf")
        else:
            comic_font_path = os.path.join(comic_dir, "ComicShannsMonoNerdFont-Regular.otf")
        
        # 如果找不到对应的字体，使用默认字体
        if not os.path.exists(comic_font_path):
            comic_font_path = comic_fonts[0]
        
        # 生成输出文件名
        output_filename = maple_filename.replace("MapleMono-NF-CN", "ChHsichNerdFont")
        output_path = os.path.join(output_dir, output_filename)
        
        try:
            process_font_pair(comic_font_path, maple_font_path, output_path)
        except Exception as e:
            print(f"处理字体 {maple_filename} 时出错: {e}")
            continue
    
    print("\nChHsich Nerd Font 创建完成!")
    print(f"输出目录: {output_dir}")

if __name__ == "__main__":
    main() 