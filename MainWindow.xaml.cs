using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Navigation;
using System.Windows.Shapes;
using System.IO;

namespace Vinyl_Collector
{
    /// <summary>
    /// Interaction logic for MainWindow.xaml
    /// </summary>
    public partial class MainWindow : Window
    {
        StringBuilder csvContent = new StringBuilder();
        string filePath = @"C:\Users\chald\source\repos\Vinyl Collector\dataTable.csv";

        public MainWindow()
        {
            InitializeComponent();
            
        }

        private void submitButton_Click(object sender, RoutedEventArgs e)
        {
            Record newRecord = new Record(titleTextBox.Text, artistTextBox.Text, labelTextBox.Text, yearTextBox.Text, lengthTextBox.Text);

            csvContent.AppendLine($"{newRecord.title}, {newRecord.artist}, {newRecord.label}, {newRecord.year}, {newRecord.length}");

            File.AppendAllText(filePath, csvContent.ToString());
            //Console.WriteLine(newRecord.title);
            //Console.WriteLine(newRecord.artist);
            //Console.WriteLine(newRecord.label);
            //Console.WriteLine(newRecord.year);
            //Console.WriteLine(newRecord.length);
            //int count = 0;
            //foreach (string line in recordTable)
            //{
            //    recordList.Text = ($"{recordTable[count]}");
            //    count++;
            //}
            Console.ReadLine();
        }

        private void clearButton_Click(object sender, RoutedEventArgs e)
        {
            titleTextBox.Text = "";
            artistTextBox.Text = "";
            labelTextBox.Text = "";
            yearTextBox.Text = "";
            lengthTextBox.Text = "";
        }
    }
}
