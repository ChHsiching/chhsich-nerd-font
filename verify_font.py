#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
验证ChHsich Nerd Font字体是否正确包含了所需的字符
"""

import fontforge
import os

def check_unicode_ranges():
    """返回需要检查的Unicode范围"""
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

def verify_font(font_path):
    """验证字体文件"""
    print(f"\n验证字体: {font_path}")
    
    try:
        font = fontforge.open(font_path)
        
        # 检查字体名称
        print(f"字体名称: {font.familyname}")
        print(f"完整名称: {font.fullname}")
        
        # 检查Unicode范围
        unicode_ranges = check_unicode_ranges()
        missing_chars = []
        found_chars = []
        
        for start_unicode, end_unicode in unicode_ranges:
            for unicode_val in range(start_unicode, end_unicode + 1):
                if unicode_val in font:
                    found_chars.append(unicode_val)
                else:
                    missing_chars.append(unicode_val)
        
        print(f"找到的字符数量: {len(found_chars)}")
        print(f"缺失的字符数量: {len(missing_chars)}")
        
        if missing_chars:
            print("缺失的字符:")
            for char in missing_chars[:10]:  # 只显示前10个
                print(f"  U+{char:04X} ({chr(char) if char < 0x10000 else '?'})")
            if len(missing_chars) > 10:
                print(f"  ... 还有 {len(missing_chars) - 10} 个字符")
        else:
            print("✓ 所有需要的字符都已包含")
        
        font.close()
        return len(missing_chars) == 0
        
    except Exception as e:
        print(f"错误: 无法打开字体文件 {font_path}: {e}")
        return False

def main():
    """主函数"""
    print("开始验证 ChHsich Nerd Font...")
    
    output_dir = "ChHsichNerdFont"
    
    if not os.path.exists(output_dir):
        print(f"错误: 输出目录 {output_dir} 不存在")
        return
    
    # 获取所有字体文件
    font_files = []
    for file in os.listdir(output_dir):
        if file.endswith('.ttf') and file.startswith('ChHsichNerdFont'):
            font_files.append(os.path.join(output_dir, file))
    
    if not font_files:
        print(f"错误: 在 {output_dir} 目录中未找到字体文件")
        return
    
    print(f"找到 {len(font_files)} 个字体文件")
    
    # 验证每个字体文件
    success_count = 0
    for font_file in sorted(font_files):
        if verify_font(font_file):
            success_count += 1
    
    print(f"\n验证完成: {success_count}/{len(font_files)} 个字体文件验证通过")
    
    if success_count == len(font_files):
        print("✓ 所有字体文件都验证通过！")
    else:
        print("⚠ 部分字体文件验证失败")

if __name__ == "__main__":
    main() 