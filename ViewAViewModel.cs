using Prism.Mvvm;
using Prism.Regions;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows;

namespace BlankApp2.ViewModels
{
    /// <summary>
    /// 
    /// ViewModel要想接收view传递过来的参数，就要继承一个接口
    /// </summary>
    public class ViewAViewModel :BindableBase, IConfirmNavigationRequest
    {
        public ViewAViewModel()
        {
            
        }
        private string block;
        public string Block
        {
            get => block;
            set
            {
                block = value;
                RaisePropertyChanged();
            }
        }

        /// <summary>
        /// 每次重新导航的时候，是否复用已经创建好的实例。
        /// </summary>
        /// <param name="navigationContext"></param>
        /// <returns></returns>
        /// <exception cref="NotImplementedException"></exception>
        public bool IsNavigationTarget(NavigationContext navigationContext)
        {
            return true;
        }


        public void OnNavigatedFrom(NavigationContext navigationContext)
        {

        }
        /// <summary>
        /// 接收View传递的信息
        /// </summary>
        /// <param name="navigationContext"></param>
        public void OnNavigatedTo(NavigationContext navigationContext)
        {
            if (navigationContext.Parameters.ContainsKey("ViewA"))
            {
                Block = navigationContext.Parameters.GetValue<string>("ViewA");
            }
        }


        /// <summary>
        /// 拦截导航请求，可以用来做路由校验
        /// </summary>
        /// <param name="navigationContext"></param>
        void IConfirmNavigationRequest.ConfirmNavigationRequest(NavigationContext navigationContext, Action<bool> continuationCallback)
        {
            Boolean result = true; 
            if(MessageBox.Show("确认导航？", "温馨提示", MessageBoxButton.YesNo) == MessageBoxResult.No)
            {
                result = false;
                continuationCallback(result);
            }
            continuationCallback(result);
        }
    }
}
