# ChHsich Nerd Font 创建工具

这个工具用于将 ComicShannsMono Nerd Font 的特定字符替换到 Maple Mono NF CN 中，创建 ChHsich Nerd Font。

## 功能

- 将 ComicShannsMono Nerd Font 的以下字符替换到 Maple Mono NF CN 中：
  - U+0021 到 U+007E (基本拉丁字母、数字和符号)
  - U+00A1 到 U+00A6 (拉丁-1补充符号)
  - U+00AB (左双角引号)
  - U+00AC (逻辑非符号)
  - U+00AF (上划线)
  - U+00B0 (度数符号)
  - U+00B1 (正负号)
  - U+00B4 (重音符)
  - U+00BB (右双角引号)
  - U+00D7 (乘号)
  - U+00F7 (除号)

## 系统要求

- Arch Linux (或其他支持 FontForge 的 Linux 发行版)
- Python 3
- FontForge

## 安装依赖

```bash
# 安装 FontForge
sudo pacman -S fontforge
```

## 使用方法

1. 确保项目目录结构如下：
   ```
   ChHsich-Nerd-Font/
   ├── ComicShannsMono/           # ComicShannsMono Nerd Font 文件
   ├── MapleMono-NF-CN-unhinted/  # Maple Mono NF CN 字体文件
   ├── ChHsichNerdFont/           # 输出目录 (空目录)
   ├── create_chhsich_nerd_font.py
   ├── test_fontforge.py
   ├── verify_font.py
   └── README.md
   ```

2. 测试 FontForge 安装：
   ```bash
   python3 test_fontforge.py
   ```

3. 运行字体创建脚本：
   ```bash
   python3 create_chhsich_nerd_font.py
   ```

4. 验证生成的字体：
   ```bash
   python3 verify_font.py
   ```

## 输出

脚本将在 `ChHsichNerdFont/` 目录中生成以下字体文件：
- ChHsichNerdFont-Regular.ttf
- ChHsichNerdFont-Bold.ttf
- ChHsichNerdFont-Italic.ttf
- ChHsichNerdFont-BoldItalic.ttf
- ChHsichNerdFont-Light.ttf
- ChHsichNerdFont-LightItalic.ttf
- ChHsichNerdFont-Medium.ttf
- ChHsichNerdFont-MediumItalic.ttf
- ChHsichNerdFont-SemiBold.ttf
- ChHsichNerdFont-SemiBoldItalic.ttf
- ChHsichNerdFont-ExtraBold.ttf
- ChHsichNerdFont-ExtraBoldItalic.ttf
- ChHsichNerdFont-Thin.ttf
- ChHsichNerdFont-ThinItalic.ttf
- ChHsichNerdFont-ExtraLight.ttf
- ChHsichNerdFont-ExtraLightItalic.ttf

## 验证结果

✅ **成功创建了16个字体文件**
- 所有字体文件都包含了所需的109个字符
- 字体名称已正确更新为 "ChHsich Nerd Font"
- 字符替换成功：ComicShannsMono Nerd Font 的英文字符已替换到 Maple Mono NF CN 中

## 注意事项

- 脚本会自动匹配字体样式（Regular、Bold、Italic等）
- 如果源字体中缺少某些字符，脚本会显示警告信息
- 生成的字体将保留 Maple Mono NF CN 的中文字符和 ComicShannsMono Nerd Font 的英文字符
- 字体名称会自动更新为 "ChHsich Nerd Font"

## 故障排除

如果遇到问题，请检查：
1. FontForge 是否正确安装
2. 字体文件是否存在于正确的目录中
3. 是否有足够的磁盘空间
4. 是否有写入权限

## 许可证

请确保遵守原始字体的许可证要求。 