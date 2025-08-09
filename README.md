# ChHsich Nerd Font 创建工具

这个工具用于将 ComicShannsMono Nerd Font 的特定字符替换到 Maple Mono NF CN 中，创建 ChHsich Nerd Font。

## 项目状态

✅ **项目已完成**
- 成功创建了16个ChHsich Nerd Font字体文件
- 所有字体都包含了所需的109个字符
- 字体名称已正确更新为"ChHsich Nerd Font"
- 字符替换成功完成
- 提供完整的安装和卸载脚本

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

### 1. 创建字体

1. 确保项目目录结构如下：
   ```
   ChHsich-Nerd-Font/
   ├── ComicShannsMono/           # ComicShannsMono Nerd Font 文件
   ├── MapleMono-NF-CN-unhinted/  # Maple Mono NF CN 字体文件
   ├── ChHsichNerdFont/           # 输出目录 (生成的字体文件)
   ├── create_chhsich_nerd_font.py
   ├── test_fontforge.py
   ├── verify_font.py
   ├── install.sh                  # 安装脚本
   ├── uninstall.sh                # 卸载脚本
   ├── LICENSE                     # 许可证文件
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

### 2. 安装字体到系统

#### 自动安装（推荐）

```bash
# 运行安装脚本
./install.sh
```

安装脚本会：
- 自动检测系统类型（Linux/macOS）
- 选择合适的字体安装目录
- 复制字体文件到系统字体目录
- 更新字体缓存
- 创建卸载脚本

#### 手动安装

```bash
# Linux系统
sudo cp -r ChHsichNerdFont/* /usr/share/fonts/ChHsichNerdFont/
sudo fc-cache -f -v

# 或者安装到用户目录
mkdir -p ~/.local/share/fonts/ChHsichNerdFont
cp -r ChHsichNerdFont/* ~/.local/share/fonts/ChHsichNerdFont/
fc-cache -f -v
```

### 3. 卸载字体

#### 自动卸载（推荐）

```bash
# 运行卸载脚本
./uninstall.sh
```

卸载脚本会：
- 自动检测字体安装位置
- 完全移除字体文件
- 更新字体缓存
- 清理残留文件

#### 手动卸载

```bash
# 如果安装在系统目录
sudo rm -rf /usr/share/fonts/ChHsichNerdFont
sudo fc-cache -f -v

# 如果安装在用户目录
rm -rf ~/.local/share/fonts/ChHsichNerdFont
fc-cache -f -v
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

## 开发历史

### 提交历史
1. **docs: 初始化项目文档** - 添加项目README文档
2. **feat: 添加FontForge测试脚本** - 创建FontForge安装验证脚本
3. **feat: 实现字体创建核心功能** - 实现主要的字体创建逻辑
4. **feat: 添加字体验证脚本** - 创建字体验证工具
5. **chore: 添加.gitignore文件** - 配置版本控制忽略规则
6. **feat: 添加源字体文件** - 添加ComicShannsMono和MapleMono源字体
7. **feat: 生成ChHsich Nerd Font字体文件** - 成功生成所有字体文件
8. **docs: 更新README文档** - 完善项目文档和开发历史
9. **feat: 添加许可证文件** - 添加SIL Open Font License 1.1许可证
10. **feat: 添加安装和卸载脚本** - 提供完整的字体安装和卸载功能

### 技术实现
- 使用FontForge Python API进行字体操作
- 实现Unicode字符范围定义和替换
- 支持批量处理多个字体文件
- 自动匹配字体样式和字重
- 提供完整的验证和测试工具
- 自动检测系统类型和字体目录
- 支持字体缓存更新和清理

## 许可证

本项目基于以下开源字体创建：

1. **ComicShannsMono Nerd Font**
   - Copyright (c) 2018 Shannon Miwa
   - Copyright (c) 2023 Jesus Gonzalez
   - Licensed under MIT License

2. **Maple Mono NF CN**
   - Copyright 2022 The Maple Mono Project Authors
   - Licensed under SIL Open Font License, Version 1.1

**ChHsich Nerd Font** 采用 SIL Open Font License, Version 1.1 许可证。

### 许可证要求：
- ✅ 可以自由使用、修改和分发
- ❌ **不能单独销售字体文件**
- ✅ 可以与其他软件捆绑分发
- ✅ 必须包含原始版权声明和许可证
- ✅ 必须使用相同的许可证

详细许可证信息请查看 [LICENSE](LICENSE) 文件。

## 注意事项

- 脚本会自动匹配字体样式（Regular、Bold、Italic等）
- 如果源字体中缺少某些字符，脚本会显示警告信息
- 生成的字体将保留 Maple Mono NF CN 的中文字符和 ComicShannsMono Nerd Font 的英文字符
- 字体名称会自动更新为 "ChHsich Nerd Font"
- **请遵守许可证要求，不要单独销售字体文件**
- 安装脚本会自动检测系统类型并选择合适的安装目录
- 卸载脚本会完全清理字体文件，不会留下残留

## 故障排除

如果遇到问题，请检查：
1. FontForge 是否正确安装
2. 字体文件是否存在于正确的目录中
3. 是否有足够的磁盘空间
4. 是否有写入权限
5. 安装脚本是否有执行权限（`chmod +x install.sh`）
6. 系统是否支持字体缓存更新（`fc-cache`命令）

## 贡献

欢迎提交Issue和Pull Request来改进这个项目。请确保遵守原始字体的许可证要求。 