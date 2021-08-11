using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace FeedbackWebApp.Models
{
    public class Feedback
    {
        public int Id { get; set; }

        public string FeedbackQ { get; set; }

        public string FeedbackA { get; set; }

        public Feedback()
        {

        }

    }
}
