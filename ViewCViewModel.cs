﻿using Prism.Services.Dialogs;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace BlankApp2.ViewModels
{
    internal class ViewCViewModel : IDialogAware
    {
        public string Title => throw new NotImplementedException();

        public event Action<IDialogResult> RequestClose;

        public bool CanCloseDialog()
        {
            return true;
        }

        public void OnDialogClosed()
        {
            RequestClose.Invoke(new DialogResult(ButtonResult.OK));
        }

        public void OnDialogOpened(IDialogParameters parameters)
        {
        }
    }
}
