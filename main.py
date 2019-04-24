# -*- coding:utf-8 -*-

from wox import Wox

class BMI(Wox):
    """BMI Calculator for Wox."""

    @staticmethod
    def bmi(weight, height):
        """计算BMI，公式是 BMI=kg/m^2"""
        try:
            weight = float(weight)
            height = float(height) / 100.0
            return weight / pow(height, 2)
        except ValueError:
            return 0

    @staticmethod
    def get_body_mass(bmi):
        """根据BMI值返回肥胖程度，依据是中国官方标准。"""
        if bmi < 18.5:
            return "Underweight"
        elif bmi < 24:
            return "Normal Weight"
        elif bmi < 28:
            return "Overweight"
        else:
            return "Obesity"

    def query(self, query):
        results = []

        keys = query.split()
        if len(keys) >= 2:
            weight, height = keys[:2]
            bmi = self.bmi(weight, height)
            if bmi:
                bmi_mass = self.get_body_mass(bmi)
                
                results.append({
                    "Title": "BMI is {:.2f}, you are {}".format(bmi, bmi_mass),
                    "SubTitle": "weight: {}kg, height: {}cm".format(weight, height),
                    "IcoPath": "Images/app.png",
                    "ContextData": "ctxData"
                })
                return results

        # 提示正确的输入格式
        results.append({
            "Title": "Valid format: weight(kg) height(cm).",
            "SubTitle": "For example: 66 168",
            "IcoPath": "Images/app.png"
        })
        return results


if __name__ == "__main__":
    BMI()

