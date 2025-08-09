#!/bin/bash

# ChHsich Nerd Font 安装脚本
# 将字体文件安装到系统字体目录

set -e

# 颜色定义
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# 字体名称
FONT_NAME="ChHsich Nerd Font"
FONT_DIR="ChHsichNerdFont"

# 检测系统类型和字体目录
detect_system() {
    if [[ "$OSTYPE" == "linux-gnu"* ]]; then
        # Linux系统
        if [[ -d "/usr/share/fonts" ]]; then
            FONT_INSTALL_DIR="/usr/share/fonts/${FONT_NAME// /}"
        elif [[ -d "/usr/local/share/fonts" ]]; then
            FONT_INSTALL_DIR="/usr/local/share/fonts/${FONT_NAME// /}"
        else
            FONT_INSTALL_DIR="$HOME/.local/share/fonts/${FONT_NAME// /}"
        fi
    elif [[ "$OSTYPE" == "darwin"* ]]; then
        # macOS系统
        FONT_INSTALL_DIR="$HOME/Library/Fonts/${FONT_NAME// /}"
    else
        echo -e "${RED}不支持的操作系统: $OSTYPE${NC}"
        exit 1
    fi
}

# 检查字体文件是否存在
check_font_files() {
    if [[ ! -d "$FONT_DIR" ]]; then
        echo -e "${RED}错误: 字体目录 '$FONT_DIR' 不存在${NC}"
        echo "请先运行字体创建脚本: python3 create_chhsich_nerd_font.py"
        exit 1
    fi

    local font_count=$(find "$FONT_DIR" -name "*.ttf" | wc -l)
    if [[ $font_count -eq 0 ]]; then
        echo -e "${RED}错误: 在 '$FONT_DIR' 目录中未找到字体文件${NC}"
        echo "请先运行字体创建脚本: python3 create_chhsich_nerd_font.py"
        exit 1
    fi

    echo -e "${GREEN}找到 $font_count 个字体文件${NC}"
}

# 检查是否已安装
check_already_installed() {
    if [[ -d "$FONT_INSTALL_DIR" ]]; then
        echo -e "${YELLOW}警告: 字体似乎已经安装在 $FONT_INSTALL_DIR${NC}"
        read -p "是否要重新安装？(y/N): " -n 1 -r
        echo
        if [[ ! $REPLY =~ ^[Yy]$ ]]; then
            echo "安装已取消"
            exit 0
        fi
        # 备份现有安装
        if [[ -d "$FONT_INSTALL_DIR" ]]; then
            BACKUP_DIR="${FONT_INSTALL_DIR}_backup_$(date +%Y%m%d_%H%M%S)"
            echo -e "${BLUE}备份现有安装到: $BACKUP_DIR${NC}"
            sudo mv "$FONT_INSTALL_DIR" "$BACKUP_DIR"
        fi
    fi
}

# 创建安装目录
create_install_dir() {
    echo -e "${BLUE}创建安装目录: $FONT_INSTALL_DIR${NC}"
    if [[ "$FONT_INSTALL_DIR" == /usr* ]]; then
        sudo mkdir -p "$FONT_INSTALL_DIR"
        sudo chown "$USER:$USER" "$FONT_INSTALL_DIR"
    else
        mkdir -p "$FONT_INSTALL_DIR"
    fi
}

# 安装字体文件
install_fonts() {
    echo -e "${BLUE}正在安装字体文件...${NC}"
    
    # 复制字体文件
    if [[ "$FONT_INSTALL_DIR" == /usr* ]]; then
        sudo cp -r "$FONT_DIR"/* "$FONT_INSTALL_DIR/"
        sudo chown -R "$USER:$USER" "$FONT_INSTALL_DIR"
    else
        cp -r "$FONT_DIR"/* "$FONT_INSTALL_DIR/"
    fi
    
    # 设置权限
    chmod 644 "$FONT_INSTALL_DIR"/*.ttf
    
    echo -e "${GREEN}字体文件安装完成${NC}"
}

# 更新字体缓存
update_font_cache() {
    echo -e "${BLUE}更新字体缓存...${NC}"
    
    if command -v fc-cache >/dev/null 2>&1; then
        if [[ "$FONT_INSTALL_DIR" == /usr* ]]; then
            sudo fc-cache -f -v
        else
            fc-cache -f -v
        fi
        echo -e "${GREEN}字体缓存更新完成${NC}"
    else
        echo -e "${YELLOW}警告: 未找到 fc-cache 命令，请手动更新字体缓存${NC}"
    fi
}

# 创建卸载脚本
create_uninstall_script() {
    local uninstall_script="$FONT_INSTALL_DIR/uninstall.sh"
    cat > "$uninstall_script" << EOF
#!/bin/bash
# ChHsich Nerd Font 卸载脚本

set -e

FONT_INSTALL_DIR="$FONT_INSTALL_DIR"
FONT_NAME="$FONT_NAME"

echo "正在卸载 \$FONT_NAME..."

if [[ -d "\$FONT_INSTALL_DIR" ]]; then
    if [[ "\$FONT_INSTALL_DIR" == /usr* ]]; then
        sudo rm -rf "\$FONT_INSTALL_DIR"
    else
        rm -rf "\$FONT_INSTALL_DIR"
    fi
    echo "字体已从 \$FONT_INSTALL_DIR 卸载"
else
    echo "字体未安装在 \$FONT_INSTALL_DIR"
fi

# 更新字体缓存
if command -v fc-cache >/dev/null 2>&1; then
    if [[ "\$FONT_INSTALL_DIR" == /usr* ]]; then
        sudo fc-cache -f -v
    else
        fc-cache -f -v
    fi
    echo "字体缓存已更新"
fi

echo "卸载完成"
EOF
    
    chmod +x "$uninstall_script"
    echo -e "${GREEN}卸载脚本已创建: $uninstall_script${NC}"
}

# 显示安装信息
show_install_info() {
    echo -e "${GREEN}================================${NC}"
    echo -e "${GREEN}  $FONT_NAME 安装完成${NC}"
    echo -e "${GREEN}================================${NC}"
    echo -e "安装位置: ${BLUE}$FONT_INSTALL_DIR${NC}"
    echo -e "字体文件数量: ${BLUE}$(find "$FONT_INSTALL_DIR" -name "*.ttf" | wc -l)${NC}"
    echo -e "卸载脚本: ${BLUE}$FONT_INSTALL_DIR/uninstall.sh${NC}"
    echo
    echo -e "${YELLOW}注意:${NC}"
    echo -e "1. 如果字体没有立即显示，请重启应用程序或系统"
    echo -e "2. 要卸载字体，请运行: ${BLUE}$FONT_INSTALL_DIR/uninstall.sh${NC}"
    echo -e "3. 字体已安装到系统字体目录，可以被所有应用程序使用"
}

# 主函数
main() {
    echo -e "${BLUE}================================${NC}"
    echo -e "${BLUE}  $FONT_NAME 安装脚本${NC}"
    echo -e "${BLUE}================================${NC}"
    echo

    # 检测系统
    detect_system
    echo -e "检测到系统类型: ${BLUE}$OSTYPE${NC}"
    echo -e "安装目录: ${BLUE}$FONT_INSTALL_DIR${NC}"
    echo

    # 检查字体文件
    check_font_files

    # 检查是否已安装
    check_already_installed

    # 创建安装目录
    create_install_dir

    # 安装字体文件
    install_fonts

    # 更新字体缓存
    update_font_cache

    # 创建卸载脚本
    create_uninstall_script

    # 显示安装信息
    show_install_info
}

# 运行主函数
main "$@" 