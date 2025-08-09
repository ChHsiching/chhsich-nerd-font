#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ChHsich Nerd Font TTC 创建脚本
将ChHsichNerdFont目录中的所有字体文件合并成一个ttc文件
"""

import os
import glob
import sys
from pathlib import Path

def check_dependencies():
    """检查必要的依赖是否已安装"""
    try:
        from fontTools import ttLib
        print("✓ fontTools 已安装")
        return True
    except ImportError:
        print("✗ fontTools 未安装")
        print("请运行: sudo pacman -S python-fonttools")
        return False

def get_font_files(font_dir):
    """获取字体目录中的所有ttf文件"""
    font_files = glob.glob(os.path.join(font_dir, "*.ttf"))
    font_files.sort()  # 按文件名排序
    return font_files

def create_ttc_file(font_files, output_path):
    """使用fontTools创建ttc文件"""
    if not font_files:
        print("错误: 未找到字体文件")
        return False
    
    print(f"找到 {len(font_files)} 个字体文件:")
    for font_file in font_files:
        print(f"  - {os.path.basename(font_file)}")
    
    try:
        from fontTools import ttLib
        
        # 创建TTCollection对象
        collection = ttLib.TTCollection()
        
        # 添加每个字体文件到集合中
        for font_file in font_files:
            print(f"正在添加字体: {os.path.basename(font_file)}")
            font = ttLib.TTFont(font_file)
            collection.fonts.append(font)
        
        # 保存为ttc文件
        print(f"\n正在创建TTC文件: {output_path}")
        collection.save(output_path)
        
        print("✓ TTC文件创建成功!")
        return True
        
    except Exception as e:
        print(f"✗ 创建TTC文件失败: {e}")
        import traceback
        traceback.print_exc()
        return False

def main():
    """主函数"""
    print("开始创建 ChHsich Nerd Font TTC 文件...")
    
    # 检查依赖
    if not check_dependencies():
        return 1
    
    # 定义路径
    font_dir = "ChHsichNerdFont"
    output_file = "ChHsichNerdFont.ttc"
    
    # 检查字体目录是否存在
    if not os.path.exists(font_dir):
        print(f"错误: 字体目录 {font_dir} 不存在")
        return 1
    
    # 获取字体文件
    font_files = get_font_files(font_dir)
    if not font_files:
        print(f"错误: 在 {font_dir} 目录中未找到.ttf字体文件")
        return 1
    
    # 创建输出目录（如果需要）
    output_dir = os.path.dirname(output_file)
    if output_dir and not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # 创建ttc文件
    if create_ttc_file(font_files, output_file):
        print(f"\n✓ TTC文件已创建: {output_file}")
        print(f"文件大小: {os.path.getsize(output_file) / (1024*1024):.1f} MB")
        print("\n现在可以在Windows上双击安装这个TTC文件来一次性安装所有字体样式!")
        return 0
    else:
        print("✗ TTC文件创建失败")
        return 1

if __name__ == "__main__":
    sys.exit(main()) 