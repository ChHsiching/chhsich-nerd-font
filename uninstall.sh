#!/bin/bash

# ChHsich Nerd Font 卸载脚本
# 从系统字体目录卸载字体文件

set -e

# 颜色定义
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# 字体名称
FONT_NAME="ChHsich Nerd Font"

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

# 检查字体是否已安装
check_font_installed() {
    if [[ ! -d "$FONT_INSTALL_DIR" ]]; then
        echo -e "${YELLOW}字体 '$FONT_NAME' 未安装在 $FONT_INSTALL_DIR${NC}"
        echo -e "${BLUE}检查其他可能的安装位置...${NC}"
        
        # 检查其他可能的安装位置
        local found=false
        for dir in "/usr/share/fonts" "/usr/local/share/fonts" "$HOME/.local/share/fonts" "$HOME/Library/Fonts"; do
            if [[ -d "$dir" ]]; then
                for font_dir in "$dir"/*; do
                    if [[ -d "$font_dir" ]] && [[ "$font_dir" == *"${FONT_NAME// /}"* ]]; then
                        echo -e "${GREEN}找到字体安装位置: $font_dir${NC}"
                        FONT_INSTALL_DIR="$font_dir"
                        found=true
                        break 2
                    fi
                done
            fi
        done
        
        if [[ "$found" == false ]]; then
            echo -e "${YELLOW}未找到已安装的字体${NC}"
            exit 0
        fi
    fi
}

# 确认卸载
confirm_uninstall() {
    echo -e "${YELLOW}即将卸载字体: $FONT_NAME${NC}"
    echo -e "安装位置: ${BLUE}$FONT_INSTALL_DIR${NC}"
    echo -e "字体文件数量: ${BLUE}$(find "$FONT_INSTALL_DIR" -name "*.ttf" 2>/dev/null | wc -l)${NC}"
    echo
    read -p "确定要卸载吗？(y/N): " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        echo -e "${BLUE}卸载已取消${NC}"
        exit 0
    fi
}

# 卸载字体文件
uninstall_fonts() {
    echo -e "${BLUE}正在卸载字体文件...${NC}"
    
    if [[ -d "$FONT_INSTALL_DIR" ]]; then
        # 检查是否有备份
        local backup_dir="${FONT_INSTALL_DIR}_backup_*"
        if ls -d $backup_dir >/dev/null 2>&1; then
            echo -e "${YELLOW}发现备份目录，是否要恢复？(y/N): ${NC}"
            read -p "" -n 1 -r
            echo
            if [[ $REPLY =~ ^[Yy]$ ]]; then
                local latest_backup=$(ls -dt $backup_dir | head -1)
                echo -e "${BLUE}恢复备份: $latest_backup${NC}"
                if [[ "$FONT_INSTALL_DIR" == /usr* ]]; then
                    sudo rm -rf "$FONT_INSTALL_DIR"
                    sudo mv "$latest_backup" "$FONT_INSTALL_DIR"
                    sudo chown -R "$USER:$USER" "$FONT_INSTALL_DIR"
                else
                    rm -rf "$FONT_INSTALL_DIR"
                    mv "$latest_backup" "$FONT_INSTALL_DIR"
                fi
                echo -e "${GREEN}备份已恢复${NC}"
                return
            fi
        fi
        
        # 卸载字体
        if [[ "$FONT_INSTALL_DIR" == /usr* ]]; then
            sudo rm -rf "$FONT_INSTALL_DIR"
        else
            rm -rf "$FONT_INSTALL_DIR"
        fi
        echo -e "${GREEN}字体已从 $FONT_INSTALL_DIR 卸载${NC}"
    else
        echo -e "${YELLOW}字体目录不存在: $FONT_INSTALL_DIR${NC}"
    fi
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

# 清理残留文件
cleanup_residual() {
    echo -e "${BLUE}清理残留文件...${NC}"
    
    # 清理可能的残留备份
    local backup_pattern="${FONT_INSTALL_DIR%/*}/${FONT_NAME// /}_backup_*"
    if ls -d $backup_pattern >/dev/null 2>&1; then
        echo -e "${YELLOW}发现备份文件，是否要删除？(y/N): ${NC}"
        read -p "" -n 1 -r
        echo
        if [[ $REPLY =~ ^[Yy]$ ]]; then
            if [[ "$FONT_INSTALL_DIR" == /usr* ]]; then
                sudo rm -rf $backup_pattern
            else
                rm -rf $backup_pattern
            fi
            echo -e "${GREEN}备份文件已清理${NC}"
        fi
    fi
}

# 显示卸载信息
show_uninstall_info() {
    echo -e "${GREEN}================================${NC}"
    echo -e "${GREEN}  $FONT_NAME 卸载完成${NC}"
    echo -e "${GREEN}================================${NC}"
    echo -e "卸载位置: ${BLUE}$FONT_INSTALL_DIR${NC}"
    echo
    echo -e "${YELLOW}注意:${NC}"
    echo -e "1. 如果字体仍然显示在应用程序中，请重启应用程序或系统"
    echo -e "2. 字体已从系统字体目录中完全移除"
    echo -e "3. 字体缓存已更新"
}

# 主函数
main() {
    echo -e "${BLUE}================================${NC}"
    echo -e "${BLUE}  $FONT_NAME 卸载脚本${NC}"
    echo -e "${BLUE}================================${NC}"
    echo

    # 检测系统
    detect_system
    echo -e "检测到系统类型: ${BLUE}$OSTYPE${NC}"
    echo -e "字体目录: ${BLUE}$FONT_INSTALL_DIR${NC}"
    echo

    # 检查字体是否已安装
    check_font_installed

    # 确认卸载
    confirm_uninstall

    # 卸载字体文件
    uninstall_fonts

    # 更新字体缓存
    update_font_cache

    # 清理残留文件
    cleanup_residual

    # 显示卸载信息
    show_uninstall_info
}

# 运行主函数
main "$@" 