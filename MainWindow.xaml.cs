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

namespace Vinyl_Collector
{
    /// <summary>
    /// Interaction logic for MainWindow.xaml
    /// </summary>
    public partial class MainWindow : Window
    {
        List<Record> recordTable = new List<Record>();
        public MainWindow()
        {
            InitializeComponent();
            
        }

        private void submitButton_Click(object sender, RoutedEventArgs e)
        {
            Record newRecord = new Record(titleTextBox.Text, artistTextBox.Text, labelTextBox.Text, yearTextBox.Text, lengthTextBox.Text);

            recordTable.Add(newRecord);
            //Console.WriteLine(newRecord.title);
            //Console.WriteLine(newRecord.artist);
            //Console.WriteLine(newRecord.label);
            //Console.WriteLine(newRecord.year);
            //Console.WriteLine(newRecord.length);
            int count = 0;
            foreach (Record line in recordTable)
            {
                Console.WriteLine($"{recordTable[count].title} {recordTable[count].artist} {recordTable[count].label} {recordTable[count].year} {recordTable[count].length}");
                count++;
            }
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
