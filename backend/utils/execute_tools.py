
from jenkinsapi.jenkins import Jenkins


class ExecuteTools:
    BASE_URL = "http://localhost:8888/"
    # BASE_URL = "http://134.175.28.202:8081/"
    USERNAME = 'admin'
    # 使用jenkins生成的token
    PASSWORD = '117b2ea9b19461871856a12520c8524d58'
    # PASSWORD = '1178bda522b3ac867e4a2dbdfcb0cd590d'
    JOB_NAME="ck18"

    @classmethod
    def get_jobs(cls):
        # 实例化jenkins
        jenkins = Jenkins(cls.BASE_URL, cls.USERNAME, cls.PASSWORD)
        # 返回所有job名称
        return jenkins.keys()

    @classmethod
    def invoke(cls, task):
        """
        调用执行器执行
        task: 指定执行的用例
        :param task:
        :return:
        """
        jenkins = Jenkins(cls.BASE_URL, cls.USERNAME, cls.PASSWORD)
        # 得到ck18job的实例对象
        job_ck18 = jenkins.get_job(cls.JOB_NAME)
        # 让你的job进行构建,需要和jenkins的job的参数名进行对应
        job_ck18.invoke(build_params={"task": task})
        # 1.Jenkins自动生成Junit.xml报告，拿到之后解析xml文件，获取用例执行的信息
        # 2.拿到allure的信息，解析json文件，获取用例的执行
        # 3.直接拿到allure的链接，就是allure的报告
        # http://localhost:8888/job/ck18/33/allure/
        # jenkins服务的信息/job/jobname/构建的数据/allure
        # 构建完成立刻获取到的构件数
        last_build_number = job_ck18.get_last_buildnumber()
        # print(last_build_number)
        while True:
            build_number = job_ck18.get_last_buildnumber()
            if last_build_number != build_number:
                # 拼接测试报告路径
                report_path = cls.BASE_URL+"job/"+cls.JOB_NAME+"/"+\
                              str(build_number)+"/allure"
                return report_path
