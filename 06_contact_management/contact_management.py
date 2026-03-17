#!/usr/bin/env python3
# 联系人管理系统

contacts = []

# 显示菜单
def show_menu():
    print("=" * 40)
    print("联系人管理系统")
    print("=" * 40)
    print("1. 添加联系人")
    print("2. 查看所有联系人")
    print("3. 搜索联系人")
    print("4. 更新联系人")
    print("5. 删除联系人")
    print("6. 保存联系人到文件")
    print("7. 从文件加载联系人")
    print("0. 退出系统")
    print("=" * 40)

# 添加联系人
def add_contact():
    name = input("请输入姓名: ")
    phone = input("请输入电话: ")
    email = input("请输入邮箱: ")
    address = input("请输入地址: ")
    
    contact = {
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    }
    
    contacts.append(contact)
    print("联系人添加成功！")

# 查看所有联系人
def view_contacts():
    if not contacts:
        print("暂无联系人")
        return
    
    print("=" * 60)
    print("联系人列表")
    print("=" * 60)
    for i, contact in enumerate(contacts, 1):
        print(f"{i}. 姓名: {contact['name']}")
        print(f"   电话: {contact['phone']}")
        print(f"   邮箱: {contact['email']}")
        print(f"   地址: {contact['address']}")
        print("-" * 60)

# 搜索联系人
def search_contact():
    keyword = input("请输入搜索关键词: ")
    results = []
    
    for contact in contacts:
        if (keyword in contact['name'] or 
            keyword in contact['phone'] or 
            keyword in contact['email'] or 
            keyword in contact['address']):
            results.append(contact)
    
    if not results:
        print("未找到匹配的联系人")
        return
    
    print("=" * 60)
    print("搜索结果")
    print("=" * 60)
    for i, contact in enumerate(results, 1):
        print(f"{i}. 姓名: {contact['name']}")
        print(f"   电话: {contact['phone']}")
        print(f"   邮箱: {contact['email']}")
        print(f"   地址: {contact['address']}")
        print("-" * 60)

# 更新联系人
def update_contact():
    name = input("请输入要更新的联系人姓名: ")
    
    for contact in contacts:
        if contact['name'] == name:
            print("当前联系人信息:")
            print(f"姓名: {contact['name']}")
            print(f"电话: {contact['phone']}")
            print(f"邮箱: {contact['email']}")
            print(f"地址: {contact['address']}")
            
            contact['phone'] = input("请输入新电话 (回车保持不变): ") or contact['phone']
            contact['email'] = input("请输入新邮箱 (回车保持不变): ") or contact['email']
            contact['address'] = input("请输入新地址 (回车保持不变): ") or contact['address']
            
            print("联系人更新成功！")
            return
    
    print("未找到该联系人")

# 删除联系人
def delete_contact():
    name = input("请输入要删除的联系人姓名: ")
    
    for i, contact in enumerate(contacts):
        if contact['name'] == name:
            confirm = input(f"确定要删除 {name} 吗？(y/n): ")
            if confirm.lower() == 'y':
                contacts.pop(i)
                print("联系人删除成功！")
            return
    
    print("未找到该联系人")

# 保存联系人到文件
def save_contacts():
    import json
    try:
        with open('contacts.json', 'w', encoding='utf-8') as f:
            json.dump(contacts, f, ensure_ascii=False, indent=2)
        print("联系人保存成功！")
    except Exception as e:
        print(f"保存失败: {e}")

# 从文件加载联系人
def load_contacts():
    import json
    try:
        with open('contacts.json', 'r', encoding='utf-8') as f:
            global contacts
            contacts = json.load(f)
        print("联系人加载成功！")
    except FileNotFoundError:
        print("文件不存在，使用空联系人列表")
    except Exception as e:
        print(f"加载失败: {e}")

# 主函数
def main():
    while True:
        show_menu()
        choice = input("请输入操作编号: ")
        
        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            update_contact()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            save_contacts()
        elif choice == '7':
            load_contacts()
        elif choice == '0':
            print("感谢使用联系人管理系统，再见！")
            break
        else:
            print("输入错误，请重新输入")
        
        input("按回车键继续...")

if __name__ == "__main__":
    main()