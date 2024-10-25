knowledge_points=['JUnit', 'Java并发数据结构', '文件扩展名', '对象成员', '单元测试', '单例模式', '方法返回类型', '文件操作', '数组访问', 'Java字符编码', 'Java并发协作控制', '入口方法', '数据类型', 'Java高级字符串处理', '字符串', 'Java异常分类', 'GUI', 'log4j', 'Java调用C程序(JNI)', 'void', '主方法', '异常处理', '列表List', '格式化相关类', '算术运算符', '关系运算符', '条形码和二维码解析', '变量', '线程', '取模运算', 'Frame', '布局管理器', '异常类', '访问控制', 'JSON解析', '构造方法', '网络应用程序', '形式参数', 'XML解析', '构造函数', '包', '运算符', '鼠标事件', '关键字', 'JCF', '表格文件解析', '集合Set', 'jar文件 导出和导入', '赋值语句', 'Java io 包', '类与对象', '继承', '覆盖', 'java源文件', 'JDBC操作', '选择语句', 'Applet', '分支语句', '字节码', '修饰符', '文本文件读写', 'Java访问权限', 'Java异常处理', '循环 语句', 'XML简介', 'Zip文件读写', '网络基础知识', '多线程同步', 'Swing', 'static和final测验', '自定义异常', '常量设计和常量池', '二进制文件读写', 'paint', '数字相关类', '三元运算符', '不可变对象和字符串', 'Thread', '基本类型', '数据库和SQL', '编译运行', '字符串相关类', 'Java多线程', 'package和import--命令行', '容器', '接口与实现类', 'static', '方法', '数组', '标识符', '映射Map', 'JDK', 'JRE', 'nan', '方法重载', '重载', '静态方法', 'Java调用Java程序(RMI)', 'Maven', '工具类', '整数', '图形图像解析', 'Java并发框架Executor', 'Java多线程信息共享', 'PDF解析', '时间相关类', 'Java TCP 编程', '进程', '堆', '字符流', '字节流', '中国特殊符号', '方法头', 'Java UDP 编程', '对象类型', 'package和import', 'Docx解析', 'Java定时任务执行', '抽象类和抽象方法', 'return', 'final', 'super', '类', '字符集', '文件系统 及Java文件基本操作', '程序编写', '顺序结构', '大整数加法', '输入输出Scanner', '字符转换', '浮点数', '数字反转', '分支结构', '数字排序', '函数与结构体', '模拟', '递归', '质数', '搜索', '排列组合', '素数', '枚举', '排序', '进制', '循环结构', '位运算', '按值传递', '变量初始化', '变量类型', '哈希表', '前缀和', '并查集', '链表', '矩阵', '双向链表', '一维动态规划', '克隆', '多维动态规划', 'Java源文件', ' 面向对象编程', '默认值', '数学', '类型转换', '贪心', '计数', '设计', '逻辑运算符', '引用传递', '引用', '双指针', '静态变量', '方法调用', '堆栈', 'Kadane 算法', '滑动窗口', '数组初始化', '分治', '动态规划', '二分查找', '运算符优先级', 'ASCLL码', '编译与运行', '栈', '布尔值']


# chapter_mapping = {
#     1: "Java概述",
#     2: "Java环境搭建和程序初体验",
#     3: "Java类基础知识",
#     4: "面向对象和类",
#     5: "继承、接口和抽象类",
#     6: "static、final和常量设计",
#     7: "package、import和classpath",
#     8: "Java常用类",
#     9: "Java异常和异常处理",
#     10: "Java数据结构",
#     11: "Java文件读写",
#     12: "Java案例实践和总结"
# }


chapter_mapping = {
    1: {
        "chapter": "Java概述",
        "knowledge_points": [
            "Java字符编码",
            "文件扩展名",
            "字符集",
            "字符转换",
            "ASCLL码",
            "Java源文件",
            "java源文件"
        ]
    },
    2: {
        "chapter": "Java环境搭建和程序初体验",
        "knowledge_points": [
            "编译运行",
            "主方法",
            "入口方法",
            "JDK",
            "JRE",
            "编译与运行"
        ]
    },
    3: {
        "chapter": "Java类基础知识",
        "knowledge_points": [
            "数据类型",
            "变量",
            "常量设计和常量池",
            "方法",
            "方法返回类型",
            "构造方法",
            "构造函数",
            "关键字",
            "标识符",
            "字节码",
            "类",
            "void",
            "nan",
            "基本类型",
            "数组",
            "数组访问",
            "赋值语句",
            "选择语句",
            "分支语句",
            "循环语句",
            "循环 语句",
            "运算符",
            "算术运算符",
            "关系运算符",
            "取模运算",
            "对象类型",
            "引用",
            "变量类型",
            "变量初始化",
            "默认值",
            "形式参数",
            "数组初始化",
            "方法头",
            "静态方法",
            "静态变量",
            "引用",
            "包",
            "Java高级字符串处理",
            "运算符优先级",
            "逻辑运算符",
            "布尔值",
            "变量初始化",
            "浮点数",
            "整数",
            "变量类型",
            "位运算",
            "三元运算符"
        ]
    },
    4: {
        "chapter": "面向对象和类",
        "knowledge_points": [
            "对象成员",
            "单例模式",
            "继承",
            "覆盖",
            "抽象类和抽象方法",
            "接口与实现类",
            "不可变对象和字符串",
            " 面向对象编程",
            "修饰符",
            "类与对象",
            "克隆",
            "super",
            "面向对象编程",
            "面向 对象编程"
        ]
    },
    5: {
        "chapter": "继承、接口和抽象类",
        "knowledge_points": [
            "继承",
            "接口与实现类"
        ]
    },
    6: {
        "chapter": "static、final和常量设计",
        "knowledge_points": [
            "static",
            "final",
            "static和final测验"
        ]
    },
    7: {
        "chapter": "package、import和classpath",
        "knowledge_points": [
            "package和import",
            "package和import--命令行"
        ]
    },
    8: {
        "chapter": "Java常用类",
        "knowledge_points": [
            "字符串",
            "数字相关类",
            "格式化相关类",
            "JSON解析",
            "XML解析",
            "Java io 包",
            "JCF",
            "log4j",
            "工具类",
            "字符流",
            "输入输出Scanner",
            "时间相关类",
            "图形图像解析",
            "字符串相关类",
            "GUI",
            "布局管理器"
        ]
    },
    9: {
        "chapter": "Java异常和异常处理",
        "knowledge_points": [
            "Java异常分类",
            "异常处理",
            "自定义异常",
            "异常类",
            "Java异常处理",
            "访问控制"
        ]
    },
    10: {
        "chapter": "Java数据结构",
        "knowledge_points": [
            "列表List",
            "集合Set",
            "映射Map",
            "容器",
            "JCF",
            "链表",
            "双向链表",
            "哈希表",
            "堆",
            "栈",
            "并查集",
            "Java并发数据结构",
            "堆栈"
        ]
    },
    11: {
        "chapter": "Java文件读写",
        "knowledge_points": [
            "文件操作",
            "文本文件读写",
            "二进制文件读写",
            "Zip文件读写",
            "中国特殊符号",
            "文件系统 及Java文件基本操作",
            "jar文件 导出和导入",
            "Docx解析",
            "字节流",
            "条形码和二维码解析",
            "表格文件解析",
            "PDF解析"
        ]
    },
    12: {
        "chapter": "Java案例实践和总结",
        "knowledge_points": [
            "动态规划",
            "递归",
            "贪心",
            "分治",
            "滑动窗口",
            "一维动态规划",
            "多维动态规划",
            "排序",
            "搜索",
            "质数",
            "函数与结构体",
            "矩阵",
            "数字排序",
            "大整数加法",
            "按值传递",
            "引用传递",
            "类型转换",
            "进制",
            "前缀和",
            "循环结构",
            "分支结构",
            "重载",
            "方法重载",
            "方法调用",
            "return",
            "设计",
            "程序编写",
            "进程",
            "线程",
            "Thread",
            "Maven",
            "网络基础知识",
            "XML简介",
            "Java并发协作控制",
            "Java多线程",
            "多线程同步",
            "排列组合",
            "双指针",
            "数字反转",
            "Java多线程信息共享",
            "Java并发框架Executor",
            "顺序结构",
            "Kadane 算法",
            "Java TCP 编程",
            "模拟",
            "二分查找",
            "计数",
            "Java UDP 编程",
            "枚举"
        ]
    },
    13: {
        "chapter": "其他",
        "knowledge_points": [
           "数学",
           "Java访问权限",
           "JUnit",
           "Swing",
           "Applet",
           "鼠标事件",
           "单元测试",
           "数据库和SQL",
           "素数",
           "网络应用程序",
           "Frame",
           "Java调用Java程序(RMI)",
           "paint",
           "JDBC操作",
           "Java调用C程序(JNI)",
           "Java定时任务执行"
        ]
    }
}





import mysql.connector
from mysql.connector import Error

# MySQL数据库连接配置
db_config = {
    'host': 'mysql.mysql',
    'database': 'sage_javon',
    'user': 'root',
    'password': 'pYRGObpCdG',
    'port': '3306'  # 默认MySQL端口
}

def get_chapter_for_knowledge(knowledge_point):
    for chapter, data in chapter_mapping.items():
        if knowledge_point in data['knowledge_points']:
            return data['chapter']
    return None

def update_exercise_chapters():
    try:
        # 连接MySQL数据库
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        # 获取所有 exercise 的 id
        cursor.execute("SELECT id FROM exercise")
        exercises = cursor.fetchall()

        for exercise in exercises:
            exercise_id = exercise[0]

            # 查找对应的 knowledge_ids
            cursor.execute("SELECT knowledge_id FROM exercise_knowledge WHERE exercise_id = %s", (exercise_id,))
            knowledge_ids = cursor.fetchall()

            knowledge_points = []
            for k_id in knowledge_ids:
                cursor.execute("SELECT name FROM knowledge WHERE id = %s", (k_id[0],))
                knowledge_point = cursor.fetchone()
                if knowledge_point:
                    knowledge_points.append(knowledge_point[0])

            # 查找章节
            chapters = set()
            for point in knowledge_points:
                chapter = get_chapter_for_knowledge(point)
                if chapter is not None:
                    chapters.add(chapter)

            # 更新章节（假设每道题目对应一个章节，这里取第一个章节作为示例）
            if chapters:
                new_chapter = list(chapters)[0]  # 取第一个章节
                cursor.execute("UPDATE exercise SET chapter = %s WHERE id = %s", (new_chapter, exercise_id))
                print(f"更新 exercise_id={exercise_id} 的章节为 {new_chapter}")

        # 提交事务
        conn.commit()
        print("所有章节更新成功")

    except Error as e:
        print(f"数据库操作错误: {e}")
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
            print("数据库连接已关闭")

# 执行更新操作
update_exercise_chapters()