using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Vinyl_Collector
{
    public class Record
    {
        public string title;
        public string artist;
        public string label;
        public string year;
        public string length;

        public Record(string aTitle, string aArtist, string aLabel, string aYear, string aLength)
        {
            title = aTitle;
            artist = aArtist;
            label = aLabel;
            year = aYear;
            length = aLength;
        }
    }
}
