using Newtonsoft.json;

namespace Company.Function
{
    public class Counter
    {
        [Jsonproperty(PropertyName="id")]
        publlic string Id {get; set;}

        [Jsonproperty(PropertyName="count")]
        public int Count {get; set;}
    }
}