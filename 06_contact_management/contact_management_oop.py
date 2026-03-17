#!/usr/bin/env python3
# 面向对象版联系人管理系统

import json

class Contact:
    """联系人类"""
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address
    
    def __str__(self):
        return f"姓名: {self.name}, 电话: {self.phone}, 邮箱: {self.email}, 地址: {self.address}"
    
    def to_dict(self):
        """转换为字典格式"""
        return {
            "name": self.name,
            "phone": self.phone,
            "email": self.email,
            "address": self.address
        }
    
    @classmethod
    def from_dict(cls, data):
        """从字典创建联系人对象"""
        return cls(
            data["name"],
            data["phone"],
            data["email"],
            data["address"]
        )

class ContactManager:
    """联系人管理类"""
    def __init__(self):
        self.contacts = []
    
    def show_menu(self):
        """显示菜单"""
        print("=" * 40)
        print("联系人管理系统 (面向对象版)")
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
    
    def add_contact(self):
        """添加联系人"""
        name = input("请输入姓名: ")
        phone = input("请输入电话: ")
        email = input("请输入邮箱: ")
        address = input("请输入地址: ")
        
        contact = Contact(name, phone, email, address)
        self.contacts.append(contact)
        print("联系人添加成功！")
    
    def view_contacts(self):
        """查看所有联系人"""
        if not self.contacts:
            print("暂无联系人")
            return
        
        print("=" * 60)
        print("联系人列表")
        print("=" * 60)
        for i, contact in enumerate(self.contacts, 1):
            print(f"{i}. 姓名: {contact.name}")
            print(f"   电话: {contact.phone}")
            print(f"   邮箱: {contact.email}")
            print(f"   地址: {contact.address}")
            print("-" * 60)
    
    def search_contact(self):
        """搜索联系人"""
        keyword = input("请输入搜索关键词: ")
        results = []
        
        for contact in self.contacts:
            if (keyword in contact.name or 
                keyword in contact.phone or 
                keyword in contact.email or 
                keyword in contact.address):
                results.append(contact)
        
        if not results:
            print("未找到匹配的联系人")
            return
        
        print("=" * 60)
        print("搜索结果")
        print("=" * 60)
        for i, contact in enumerate(results, 1):
            print(f"{i}. 姓名: {contact.name}")
            print(f"   电话: {contact.phone}")
            print(f"   邮箱: {contact.email}")
            print(f"   地址: {contact.address}")
            print("-" * 60)
    
    def update_contact(self):
        """更新联系人"""
        name = input("请输入要更新的联系人姓名: ")
        
        for contact in self.contacts:
            if contact.name == name:
                print("当前联系人信息:")
                print(f"姓名: {contact.name}")
                print(f"电话: {contact.phone}")
                print(f"邮箱: {contact.email}")
                print(f"地址: {contact.address}")
                
                contact.phone = input("请输入新电话 (回车保持不变): ") or contact.phone
                contact.email = input("请输入新邮箱 (回车保持不变): ") or contact.email
                contact.address = input("请输入新地址 (回车保持不变): ") or contact.address
                
                print("联系人更新成功！")
                return
        
        print("未找到该联系人")
    
    def delete_contact(self):
        """删除联系人"""
        name = input("请输入要删除的联系人姓名: ")
        
        for i, contact in enumerate(self.contacts):
            if contact.name == name:
                confirm = input(f"确定要删除 {name} 吗？(y/n): ")
                if confirm.lower() == 'y':
                    self.contacts.pop(i)
                    print("联系人删除成功！")
                return
        
        print("未找到该联系人")
    
    def save_contacts(self):
        """保存联系人到文件"""
        try:
            contacts_data = [contact.to_dict() for contact in self.contacts]
            with open('contacts.json', 'w', encoding='utf-8') as f:
                json.dump(contacts_data, f, ensure_ascii=False, indent=2)
            print("联系人保存成功！")
        except Exception as e:
            print(f"保存失败: {e}")
    
    def load_contacts(self):
        """从文件加载联系人"""
        try:
            with open('contacts.json', 'r', encoding='utf-8') as f:
                contacts_data = json.load(f)
            self.contacts = [Contact.from_dict(data) for data in contacts_data]
            print("联系人加载成功！")
        except FileNotFoundError:
            print("文件不存在，使用空联系人列表")
        except Exception as e:
            print(f"加载失败: {e}")
    
    def run(self):
        """运行系统"""
        while True:
            self.show_menu()
            choice = input("请输入操作编号: ")
            
            if choice == '1':
                self.add_contact()
            elif choice == '2':
                self.view_contacts()
            elif choice == '3':
                self.search_contact()
            elif choice == '4':
                self.update_contact()
            elif choice == '5':
                self.delete_contact()
            elif choice == '6':
                self.save_contacts()
            elif choice == '7':
                self.load_contacts()
            elif choice == '0':
                print("感谢使用联系人管理系统，再见！")
                break
            else:
                print("输入错误，请重新输入")
            
            input("按回车键继续...")

if __name__ == "__main__":
    manager = ContactManager()
    manager.run()