#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
测试TTC文件的脚本
验证TTC文件是否包含所有预期的字体样式
"""

import os
import sys
from fontTools import ttLib

def test_ttc_file(ttc_path):
    """测试TTC文件"""
    if not os.path.exists(ttc_path):
        print(f"错误: TTC文件 {ttc_path} 不存在")
        return False
    
    try:
        # 打开TTC文件
        collection = ttLib.TTCollection(ttc_path)
        
        print(f"✓ TTC文件加载成功: {ttc_path}")
        print(f"包含 {len(collection.fonts)} 个字体:")
        
        # 检查每个字体
        expected_fonts = [
            "ChHsich Nerd Font Thin",
            "ChHsich Nerd Font Thin Italic", 
            "ChHsich Nerd Font ExtraLight",
            "ChHsich Nerd Font ExtraLight Italic",
            "ChHsich Nerd Font Light",
            "ChHsich Nerd Font Light Italic",
            "ChHsich Nerd Font Regular",
            "ChHsich Nerd Font Italic",
            "ChHsich Nerd Font Medium",
            "ChHsich Nerd Font Medium Italic",
            "ChHsich Nerd Font SemiBold",
            "ChHsich Nerd Font SemiBold Italic",
            "ChHsich Nerd Font Bold",
            "ChHsich Nerd Font Bold Italic",
            "ChHsich Nerd Font ExtraBold",
            "ChHsich Nerd Font ExtraBold Italic"
        ]
        
        found_fonts = []
        for i, font in enumerate(collection.fonts):
            try:
                # 获取字体名称
                name_table = font['name']
                font_name = name_table.getDebugName(4)  # Full name
                if not font_name:
                    font_name = name_table.getDebugName(1)  # Family name
                
                found_fonts.append(font_name)
                print(f"  {i+1:2d}. {font_name}")
                
            except Exception as e:
                print(f"  {i+1:2d}. 无法获取字体名称: {e}")
        
        # 检查是否包含所有预期字体
        missing_fonts = []
        for expected in expected_fonts:
            if not any(expected in found for found in found_fonts):
                missing_fonts.append(expected)
        
        if missing_fonts:
            print(f"\n⚠️  缺少以下字体:")
            for missing in missing_fonts:
                print(f"  - {missing}")
            return False
        else:
            print(f"\n✓ 所有预期的字体都已包含在TTC文件中")
            return True
            
    except Exception as e:
        print(f"✗ 测试TTC文件失败: {e}")
        import traceback
        traceback.print_exc()
        return False

def main():
    """主函数"""
    ttc_file = "ChHsichNerdFont.ttc"
    
    print("开始测试TTC文件...")
    
    if test_ttc_file(ttc_file):
        print("\n✅ TTC文件测试通过!")
        print("文件已准备好供Windows用户使用。")
        return 0
    else:
        print("\n❌ TTC文件测试失败!")
        return 1

if __name__ == "__main__":
    sys.exit(main()) 