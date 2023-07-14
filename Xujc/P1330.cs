using System;

namespace MortgageCalculator
{
    class Program
    {
        static void Main(string[] args)
        {
            // 读取输入数据
            int n = int.Parse(Console.ReadLine()); // 测试数据的行数
            for (int i = 0; i < n; i++)
            {
                string[] input = Console.ReadLine().Split(); // 每行输入的三个数字
                double loanAmount = double.Parse(input[0]); // 借款金额
                double interestRate = double.Parse(input[1]) / 100; // 利率百分比
                int loanTerm = int.Parse(input[2]); // 还款年数

                // 计算每月应还金额
                double monthlyInterestRate = interestRate / 12; // 每月利率
                int numberOfPayments = loanTerm * 12; // 总共还款次数
                double monthlyPayment = (loanAmount * monthlyInterestRate) / (1 - Math.Pow(1 + monthlyInterestRate, -numberOfPayments)); // 每月应还金额

                // 输出结果，四舍五入到最近的整数
                Console.WriteLine(Math.Round(monthlyPayment));
            }
        }
    }
}