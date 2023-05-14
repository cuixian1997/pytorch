using BlankApp2.Views;
using Prism.Commands;
using Prism.Mvvm;
using Prism.Regions;
using Prism.Services.Dialogs;
using System;
using System.Reflection;
using System.Security.Cryptography;
using System.Windows.Media;
using System.Windows.Media.Animation;

namespace BlankApp2.ViewModels
{
    public class MainViewModel : BindableBase
    {
        private string _title = "Prism Application";
        public string Title
        {
            get { return _title; }
            set { SetProperty(ref _title, value); }
        }

        private IRegionManager regionManager;
        public IDialogService dialogService { get; set; }
        public DelegateCommand<string> OpenCommand { get; private set; }
        public MainViewModel(IRegionManager regionManager, IDialogService dialogService)
        {
            OpenCommand = new DelegateCommand<string>(Open);
            this.regionManager = regionManager;
            this.dialogService = dialogService;
        }
        /// <summary>
        /// 首先通过IRegionManager接口获得当前定义的可用区域：regionManager.Regions["ContentRegion"]
        /// 我们在前端已经定义好了区域。
        /// 往这个区域中动态地设置内容，设置内容的方式是依赖注入，在App中注册控件。
        /// RequestNavigate接收：控件，控件对应的viewMode，传递的参数l
        /// </summary>
        /// <param name="obj"></param>
        private void Open(string obj)
        {
            // 弹窗ViewC，但不要用new对象的方式。应该优先考虑依赖注入
            // new ViewC().ShowDialog();
            NavigationParameters keys = new NavigationParameters();
            if (obj.Equals("ViewA") || obj.Equals("ViewB")) 
            {
                string _key = obj;
                string _val = "我是" + obj;
                keys.Add(_key, _val);
                regionManager.Regions["ContentRegion"].RequestNavigate(obj, keys);
             }
            else
            {
                dialogService.ShowDialog(obj);
            }
        }
    }
}