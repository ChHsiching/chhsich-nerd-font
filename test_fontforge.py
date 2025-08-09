#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
测试FontForge是否正确安装
"""

try:
    import fontforge
    print("✓ FontForge已正确安装")
    print(f"FontForge版本: {fontforge.version()}")
except ImportError as e:
    print("✗ FontForge未安装或无法导入")
    print(f"错误信息: {e}")
    print("\n请确保已安装FontForge:")
    print("在Arch Linux上运行: sudo pacman -S fontforge")
    exit(1)

# 测试基本功能
try:
    # 创建一个简单的测试字体
    test_font = fontforge.font()
    print("✓ FontForge基本功能正常")
    test_font.close()
except Exception as e:
    print(f"✗ FontForge基本功能测试失败: {e}")
    exit(1)

print("\nFontForge测试完成，可以运行主脚本了！") 