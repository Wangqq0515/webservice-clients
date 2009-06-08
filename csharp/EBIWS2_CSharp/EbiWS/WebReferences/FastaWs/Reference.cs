// ------------------------------------------------------------------------------
//  <autogenerated>
//      This code was generated by a tool.
//      Mono Runtime Version: 2.0.50727.42
// 
//      Changes to this file may cause incorrect behavior and will be lost if 
//      the code is regenerated.
//  </autogenerated>
// ------------------------------------------------------------------------------

namespace EbiWS.FastaWs {
    
    
    /// <remarks/>
    [System.Web.Services.WebServiceBinding(Name="JDispatcherServiceHttpPort", Namespace="http://soap.jdispatcher.ebi.ac.uk")]
    [System.Diagnostics.DebuggerStepThroughAttribute()]
    [System.ComponentModel.DesignerCategoryAttribute("code")]
    public partial class JDispatcherService : System.Web.Services.Protocols.SoapHttpClientProtocol {
        
        private System.Threading.SendOrPostCallback runOperationCompleted;
        
        private System.Threading.SendOrPostCallback getStatusOperationCompleted;
        
        private System.Threading.SendOrPostCallback getResultTypesOperationCompleted;
        
        private System.Threading.SendOrPostCallback getResultOperationCompleted;
        
        private System.Threading.SendOrPostCallback getParametersOperationCompleted;
        
        private System.Threading.SendOrPostCallback getParameterDetailsOperationCompleted;
        
        public JDispatcherService() {
            this.Url = "http://wwwdev.ebi.ac.uk/Tools/services/soap/fasta";
        }
        
        public JDispatcherService(string url) {
            this.Url = url;
        }
        
        public event runCompletedEventHandler runCompleted;
        
        public event getStatusCompletedEventHandler getStatusCompleted;
        
        public event getResultTypesCompletedEventHandler getResultTypesCompleted;
        
        public event getResultCompletedEventHandler getResultCompleted;
        
        public event getParametersCompletedEventHandler getParametersCompleted;
        
        public event getParameterDetailsCompletedEventHandler getParameterDetailsCompleted;
        
        [System.Web.Services.Protocols.SoapDocumentMethodAttribute("urn:Run", RequestNamespace="http://soap.jdispatcher.ebi.ac.uk", ResponseNamespace="http://soap.jdispatcher.ebi.ac.uk", ParameterStyle=System.Web.Services.Protocols.SoapParameterStyle.Wrapped, Use=System.Web.Services.Description.SoapBindingUse.Literal)]
        [return: System.Xml.Serialization.XmlElementAttribute("jobId")]
        public string run(string email, [System.Xml.Serialization.XmlElementAttribute(IsNullable=true)] string title, InputParameters parameters) {
            object[] results = this.Invoke("run", new object[] {
                        email,
                        title,
                        parameters});
            return ((string)(results[0]));
        }
        
        public System.IAsyncResult Beginrun(string email, string title, InputParameters parameters, System.AsyncCallback callback, object asyncState) {
            return this.BeginInvoke("run", new object[] {
                        email,
                        title,
                        parameters}, callback, asyncState);
        }
        
        public string Endrun(System.IAsyncResult asyncResult) {
            object[] results = this.EndInvoke(asyncResult);
            return ((string)(results[0]));
        }
        
        public void runAsync(string email, string title, InputParameters parameters) {
            this.runAsync(email, title, parameters, null);
        }
        
        public void runAsync(string email, string title, InputParameters parameters, object userState) {
            if ((this.runOperationCompleted == null)) {
                this.runOperationCompleted = new System.Threading.SendOrPostCallback(this.OnrunCompleted);
            }
            this.InvokeAsync("run", new object[] {
                        email,
                        title,
                        parameters}, this.runOperationCompleted, userState);
        }
        
        private void OnrunCompleted(object arg) {
            if ((this.runCompleted != null)) {
                System.Web.Services.Protocols.InvokeCompletedEventArgs invokeArgs = ((System.Web.Services.Protocols.InvokeCompletedEventArgs)(arg));
                this.runCompleted(this, new runCompletedEventArgs(invokeArgs.Results, invokeArgs.Error, invokeArgs.Cancelled, invokeArgs.UserState));
            }
        }
        
        [System.Web.Services.Protocols.SoapDocumentMethodAttribute("urn:GetStatus", RequestNamespace="http://soap.jdispatcher.ebi.ac.uk", ResponseNamespace="http://soap.jdispatcher.ebi.ac.uk", ParameterStyle=System.Web.Services.Protocols.SoapParameterStyle.Wrapped, Use=System.Web.Services.Description.SoapBindingUse.Literal)]
        [return: System.Xml.Serialization.XmlElementAttribute("status")]
        public string getStatus(string jobId) {
            object[] results = this.Invoke("getStatus", new object[] {
                        jobId});
            return ((string)(results[0]));
        }
        
        public System.IAsyncResult BegingetStatus(string jobId, System.AsyncCallback callback, object asyncState) {
            return this.BeginInvoke("getStatus", new object[] {
                        jobId}, callback, asyncState);
        }
        
        public string EndgetStatus(System.IAsyncResult asyncResult) {
            object[] results = this.EndInvoke(asyncResult);
            return ((string)(results[0]));
        }
        
        public void getStatusAsync(string jobId) {
            this.getStatusAsync(jobId, null);
        }
        
        public void getStatusAsync(string jobId, object userState) {
            if ((this.getStatusOperationCompleted == null)) {
                this.getStatusOperationCompleted = new System.Threading.SendOrPostCallback(this.OngetStatusCompleted);
            }
            this.InvokeAsync("getStatus", new object[] {
                        jobId}, this.getStatusOperationCompleted, userState);
        }
        
        private void OngetStatusCompleted(object arg) {
            if ((this.getStatusCompleted != null)) {
                System.Web.Services.Protocols.InvokeCompletedEventArgs invokeArgs = ((System.Web.Services.Protocols.InvokeCompletedEventArgs)(arg));
                this.getStatusCompleted(this, new getStatusCompletedEventArgs(invokeArgs.Results, invokeArgs.Error, invokeArgs.Cancelled, invokeArgs.UserState));
            }
        }
        
        [System.Web.Services.Protocols.SoapDocumentMethodAttribute("urn:GetResultTypes", RequestNamespace="http://soap.jdispatcher.ebi.ac.uk", ResponseNamespace="http://soap.jdispatcher.ebi.ac.uk", ParameterStyle=System.Web.Services.Protocols.SoapParameterStyle.Wrapped, Use=System.Web.Services.Description.SoapBindingUse.Literal)]
        [return: System.Xml.Serialization.XmlArray(ElementName="resultTypes")]
        [return: System.Xml.Serialization.XmlArrayItem(ElementName="type", IsNullable=false)]
        public wsResultType[] getResultTypes(string jobId) {
            object[] results = this.Invoke("getResultTypes", new object[] {
                        jobId});
            return ((wsResultType[])(results[0]));
        }
        
        public System.IAsyncResult BegingetResultTypes(string jobId, System.AsyncCallback callback, object asyncState) {
            return this.BeginInvoke("getResultTypes", new object[] {
                        jobId}, callback, asyncState);
        }
        
        public wsResultType[] EndgetResultTypes(System.IAsyncResult asyncResult) {
            object[] results = this.EndInvoke(asyncResult);
            return ((wsResultType[])(results[0]));
        }
        
        public void getResultTypesAsync(string jobId) {
            this.getResultTypesAsync(jobId, null);
        }
        
        public void getResultTypesAsync(string jobId, object userState) {
            if ((this.getResultTypesOperationCompleted == null)) {
                this.getResultTypesOperationCompleted = new System.Threading.SendOrPostCallback(this.OngetResultTypesCompleted);
            }
            this.InvokeAsync("getResultTypes", new object[] {
                        jobId}, this.getResultTypesOperationCompleted, userState);
        }
        
        private void OngetResultTypesCompleted(object arg) {
            if ((this.getResultTypesCompleted != null)) {
                System.Web.Services.Protocols.InvokeCompletedEventArgs invokeArgs = ((System.Web.Services.Protocols.InvokeCompletedEventArgs)(arg));
                this.getResultTypesCompleted(this, new getResultTypesCompletedEventArgs(invokeArgs.Results, invokeArgs.Error, invokeArgs.Cancelled, invokeArgs.UserState));
            }
        }
        
        [System.Web.Services.Protocols.SoapDocumentMethodAttribute("urn:GetResult", RequestNamespace="http://soap.jdispatcher.ebi.ac.uk", ResponseNamespace="http://soap.jdispatcher.ebi.ac.uk", ParameterStyle=System.Web.Services.Protocols.SoapParameterStyle.Wrapped, Use=System.Web.Services.Description.SoapBindingUse.Literal)]
        [return: System.Xml.Serialization.XmlElementAttribute("output", IsNullable=true)]
        public byte[] getResult(string jobId, string type, [System.Xml.Serialization.XmlArray(IsNullable=true)] [System.Xml.Serialization.XmlArrayItem(ElementName="parameter", IsNullable=false)] wsRawOutputParameter[] parameters) {
            object[] results = this.Invoke("getResult", new object[] {
                        jobId,
                        type,
                        parameters});
            return ((byte[])(results[0]));
        }
        
        public System.IAsyncResult BegingetResult(string jobId, string type, wsRawOutputParameter[] parameters, System.AsyncCallback callback, object asyncState) {
            return this.BeginInvoke("getResult", new object[] {
                        jobId,
                        type,
                        parameters}, callback, asyncState);
        }
        
        public byte[] EndgetResult(System.IAsyncResult asyncResult) {
            object[] results = this.EndInvoke(asyncResult);
            return ((byte[])(results[0]));
        }
        
        public void getResultAsync(string jobId, string type, wsRawOutputParameter[] parameters) {
            this.getResultAsync(jobId, type, parameters, null);
        }
        
        public void getResultAsync(string jobId, string type, wsRawOutputParameter[] parameters, object userState) {
            if ((this.getResultOperationCompleted == null)) {
                this.getResultOperationCompleted = new System.Threading.SendOrPostCallback(this.OngetResultCompleted);
            }
            this.InvokeAsync("getResult", new object[] {
                        jobId,
                        type,
                        parameters}, this.getResultOperationCompleted, userState);
        }
        
        private void OngetResultCompleted(object arg) {
            if ((this.getResultCompleted != null)) {
                System.Web.Services.Protocols.InvokeCompletedEventArgs invokeArgs = ((System.Web.Services.Protocols.InvokeCompletedEventArgs)(arg));
                this.getResultCompleted(this, new getResultCompletedEventArgs(invokeArgs.Results, invokeArgs.Error, invokeArgs.Cancelled, invokeArgs.UserState));
            }
        }
        
        [System.Web.Services.Protocols.SoapDocumentMethodAttribute("urn:GetParameters", RequestNamespace="http://soap.jdispatcher.ebi.ac.uk", ResponseNamespace="http://soap.jdispatcher.ebi.ac.uk", ParameterStyle=System.Web.Services.Protocols.SoapParameterStyle.Wrapped, Use=System.Web.Services.Description.SoapBindingUse.Literal)]
        [return: System.Xml.Serialization.XmlArray(ElementName="parameters")]
        [return: System.Xml.Serialization.XmlArrayItem(ElementName="id", IsNullable=false)]
        public string[] getParameters() {
            object[] results = this.Invoke("getParameters", new object[0]);
            return ((string[])(results[0]));
        }
        
        public System.IAsyncResult BegingetParameters(System.AsyncCallback callback, object asyncState) {
            return this.BeginInvoke("getParameters", new object[0], callback, asyncState);
        }
        
        public string[] EndgetParameters(System.IAsyncResult asyncResult) {
            object[] results = this.EndInvoke(asyncResult);
            return ((string[])(results[0]));
        }
        
        public void getParametersAsync() {
            this.getParametersAsync(null);
        }
        
        public void getParametersAsync(object userState) {
            if ((this.getParametersOperationCompleted == null)) {
                this.getParametersOperationCompleted = new System.Threading.SendOrPostCallback(this.OngetParametersCompleted);
            }
            this.InvokeAsync("getParameters", new object[0], this.getParametersOperationCompleted, userState);
        }
        
        private void OngetParametersCompleted(object arg) {
            if ((this.getParametersCompleted != null)) {
                System.Web.Services.Protocols.InvokeCompletedEventArgs invokeArgs = ((System.Web.Services.Protocols.InvokeCompletedEventArgs)(arg));
                this.getParametersCompleted(this, new getParametersCompletedEventArgs(invokeArgs.Results, invokeArgs.Error, invokeArgs.Cancelled, invokeArgs.UserState));
            }
        }
        
        [System.Web.Services.Protocols.SoapDocumentMethodAttribute("urn:GetParameterDetails", RequestNamespace="http://soap.jdispatcher.ebi.ac.uk", ResponseNamespace="http://soap.jdispatcher.ebi.ac.uk", ParameterStyle=System.Web.Services.Protocols.SoapParameterStyle.Wrapped, Use=System.Web.Services.Description.SoapBindingUse.Literal)]
        [return: System.Xml.Serialization.XmlElementAttribute("parameterDetails")]
        public wsParameterDetails getParameterDetails(string parameterId) {
            object[] results = this.Invoke("getParameterDetails", new object[] {
                        parameterId});
            return ((wsParameterDetails)(results[0]));
        }
        
        public System.IAsyncResult BegingetParameterDetails(string parameterId, System.AsyncCallback callback, object asyncState) {
            return this.BeginInvoke("getParameterDetails", new object[] {
                        parameterId}, callback, asyncState);
        }
        
        public wsParameterDetails EndgetParameterDetails(System.IAsyncResult asyncResult) {
            object[] results = this.EndInvoke(asyncResult);
            return ((wsParameterDetails)(results[0]));
        }
        
        public void getParameterDetailsAsync(string parameterId) {
            this.getParameterDetailsAsync(parameterId, null);
        }
        
        public void getParameterDetailsAsync(string parameterId, object userState) {
            if ((this.getParameterDetailsOperationCompleted == null)) {
                this.getParameterDetailsOperationCompleted = new System.Threading.SendOrPostCallback(this.OngetParameterDetailsCompleted);
            }
            this.InvokeAsync("getParameterDetails", new object[] {
                        parameterId}, this.getParameterDetailsOperationCompleted, userState);
        }
        
        private void OngetParameterDetailsCompleted(object arg) {
            if ((this.getParameterDetailsCompleted != null)) {
                System.Web.Services.Protocols.InvokeCompletedEventArgs invokeArgs = ((System.Web.Services.Protocols.InvokeCompletedEventArgs)(arg));
                this.getParameterDetailsCompleted(this, new getParameterDetailsCompletedEventArgs(invokeArgs.Results, invokeArgs.Error, invokeArgs.Cancelled, invokeArgs.UserState));
            }
        }
    }
    
    /// <remarks/>
    [System.CodeDom.Compiler.GeneratedCodeAttribute("System.Xml", "2.0.50727.42")]
    [System.SerializableAttribute()]
    [System.Diagnostics.DebuggerStepThroughAttribute()]
    [System.ComponentModel.DesignerCategoryAttribute("code")]
    [System.Xml.Serialization.XmlTypeAttribute(Namespace="http://soap.jdispatcher.ebi.ac.uk")]
    public partial class InputParameters {
        
        /// <remarks/>
        public string program;
        
        /// <remarks/>
        public string stype;
        
        /// <remarks/>
        [System.Xml.Serialization.XmlElementAttribute(IsNullable=true)]
        public string matrix;
        
        /// <remarks/>
        [System.Xml.Serialization.XmlElementAttribute(IsNullable=true)]
        public string gapopen;
        
        /// <remarks/>
        [System.Xml.Serialization.XmlElementAttribute(IsNullable=true)]
        public string gapext;
        
        /// <remarks/>
        [System.Xml.Serialization.XmlElementAttribute(IsNullable=true)]
        public string expupperlim;
        
        /// <remarks/>
        [System.Xml.Serialization.XmlElementAttribute(IsNullable=true)]
        public string explowlim;
        
        /// <remarks/>
        [System.Xml.Serialization.XmlElementAttribute(IsNullable=true)]
        public string strand;
        
        /// <remarks/>
        [System.Xml.Serialization.XmlElementAttribute(IsNullable=true, DataType="boolean")]
        public System.Nullable<bool> hist;
        
        /// <remarks/>
        [System.Xml.Serialization.XmlIgnore()]
        public bool histSpecified;
        
        /// <remarks/>
        [System.Xml.Serialization.XmlElementAttribute(IsNullable=true)]
        public string scores;
        
        /// <remarks/>
        [System.Xml.Serialization.XmlElementAttribute(IsNullable=true)]
        public string alignments;
        
        /// <remarks/>
        [System.Xml.Serialization.XmlElementAttribute(IsNullable=true)]
        public string seqrange;
        
        /// <remarks/>
        [System.Xml.Serialization.XmlElementAttribute(IsNullable=true)]
        public string dbrange;
        
        /// <remarks/>
        [System.Xml.Serialization.XmlElementAttribute(IsNullable=true)]
        public string filter;
        
        /// <remarks/>
        [System.Xml.Serialization.XmlElementAttribute(IsNullable=true)]
        public string stats;
        
        /// <remarks/>
        public string sequence;
        
        /// <remarks/>
        public string[] database;
        
        /// <remarks/>
        [System.Xml.Serialization.XmlElementAttribute(IsNullable=true)]
        public string ktup;
    }
    
    /// <remarks/>
    [System.CodeDom.Compiler.GeneratedCodeAttribute("System.Xml", "2.0.50727.42")]
    [System.SerializableAttribute()]
    [System.Diagnostics.DebuggerStepThroughAttribute()]
    [System.ComponentModel.DesignerCategoryAttribute("code")]
    [System.Xml.Serialization.XmlTypeAttribute(Namespace="http://soap.jdispatcher.ebi.ac.uk")]
    public partial class wsResultType {
        
        /// <remarks/>
        [System.Xml.Serialization.XmlElementAttribute(IsNullable=true)]
        public string description;
        
        /// <remarks/>
        public string fileSuffix;
        
        /// <remarks/>
        public string identifier;
        
        /// <remarks/>
        [System.Xml.Serialization.XmlElementAttribute(IsNullable=true)]
        public string label;
        
        /// <remarks/>
        public string mediaType;
    }
    
    /// <remarks/>
    [System.CodeDom.Compiler.GeneratedCodeAttribute("System.Xml", "2.0.50727.42")]
    [System.SerializableAttribute()]
    [System.Diagnostics.DebuggerStepThroughAttribute()]
    [System.ComponentModel.DesignerCategoryAttribute("code")]
    [System.Xml.Serialization.XmlTypeAttribute(Namespace="http://soap.jdispatcher.ebi.ac.uk")]
    public partial class wsRawOutputParameter {
        
        /// <remarks/>
        public string name;
        
        /// <remarks/>
        public string[] value;
    }
    
    /// <remarks/>
    [System.CodeDom.Compiler.GeneratedCodeAttribute("System.Xml", "2.0.50727.42")]
    [System.SerializableAttribute()]
    [System.Diagnostics.DebuggerStepThroughAttribute()]
    [System.ComponentModel.DesignerCategoryAttribute("code")]
    [System.Xml.Serialization.XmlTypeAttribute(Namespace="http://soap.jdispatcher.ebi.ac.uk")]
    public partial class wsParameterDetails {
        
        /// <remarks/>
        public string name;
        
        /// <remarks/>
        public string description;
        
        /// <remarks/>
        public string type;
        
        /// <remarks/>
        [System.Xml.Serialization.XmlArrayItem(ElementName="value", IsNullable=false)]
        public wsParameterValue[] values;
    }
    
    /// <remarks/>
    [System.CodeDom.Compiler.GeneratedCodeAttribute("System.Xml", "2.0.50727.42")]
    [System.SerializableAttribute()]
    [System.Diagnostics.DebuggerStepThroughAttribute()]
    [System.ComponentModel.DesignerCategoryAttribute("code")]
    [System.Xml.Serialization.XmlTypeAttribute(Namespace="http://soap.jdispatcher.ebi.ac.uk")]
    public partial class wsParameterValue {
        
        /// <remarks/>
        public string label;
        
        /// <remarks/>
        public string value;
        
        /// <remarks/>
        public bool defaultValue;
        
        /// <remarks/>
        [System.Xml.Serialization.XmlArrayItem(ElementName="property", IsNullable=false)]
        public wsProperty[] properties;
    }
    
    /// <remarks/>
    [System.CodeDom.Compiler.GeneratedCodeAttribute("System.Xml", "2.0.50727.42")]
    [System.SerializableAttribute()]
    [System.Diagnostics.DebuggerStepThroughAttribute()]
    [System.ComponentModel.DesignerCategoryAttribute("code")]
    [System.Xml.Serialization.XmlTypeAttribute(Namespace="http://soap.jdispatcher.ebi.ac.uk")]
    public partial class wsProperty {
        
        /// <remarks/>
        public string key;
        
        /// <remarks/>
        public string value;
    }
    
    public partial class runCompletedEventArgs : System.ComponentModel.AsyncCompletedEventArgs {
        
        private object[] results;
        
        internal runCompletedEventArgs(object[] results, System.Exception exception, bool cancelled, object userState) : 
                base(exception, cancelled, userState) {
            this.results = results;
        }
        
        public string Result {
            get {
                this.RaiseExceptionIfNecessary();
                return ((string)(this.results[0]));
            }
        }
    }
    
    public delegate void runCompletedEventHandler(object sender, runCompletedEventArgs args);
    
    public partial class getStatusCompletedEventArgs : System.ComponentModel.AsyncCompletedEventArgs {
        
        private object[] results;
        
        internal getStatusCompletedEventArgs(object[] results, System.Exception exception, bool cancelled, object userState) : 
                base(exception, cancelled, userState) {
            this.results = results;
        }
        
        public string Result {
            get {
                this.RaiseExceptionIfNecessary();
                return ((string)(this.results[0]));
            }
        }
    }
    
    public delegate void getStatusCompletedEventHandler(object sender, getStatusCompletedEventArgs args);
    
    public partial class getResultTypesCompletedEventArgs : System.ComponentModel.AsyncCompletedEventArgs {
        
        private object[] results;
        
        internal getResultTypesCompletedEventArgs(object[] results, System.Exception exception, bool cancelled, object userState) : 
                base(exception, cancelled, userState) {
            this.results = results;
        }
        
        public wsResultType[] Result {
            get {
                this.RaiseExceptionIfNecessary();
                return ((wsResultType[])(this.results[0]));
            }
        }
    }
    
    public delegate void getResultTypesCompletedEventHandler(object sender, getResultTypesCompletedEventArgs args);
    
    public partial class getResultCompletedEventArgs : System.ComponentModel.AsyncCompletedEventArgs {
        
        private object[] results;
        
        internal getResultCompletedEventArgs(object[] results, System.Exception exception, bool cancelled, object userState) : 
                base(exception, cancelled, userState) {
            this.results = results;
        }
        
        public byte[] Result {
            get {
                this.RaiseExceptionIfNecessary();
                return ((byte[])(this.results[0]));
            }
        }
    }
    
    public delegate void getResultCompletedEventHandler(object sender, getResultCompletedEventArgs args);
    
    public partial class getParametersCompletedEventArgs : System.ComponentModel.AsyncCompletedEventArgs {
        
        private object[] results;
        
        internal getParametersCompletedEventArgs(object[] results, System.Exception exception, bool cancelled, object userState) : 
                base(exception, cancelled, userState) {
            this.results = results;
        }
        
        public string[] Result {
            get {
                this.RaiseExceptionIfNecessary();
                return ((string[])(this.results[0]));
            }
        }
    }
    
    public delegate void getParametersCompletedEventHandler(object sender, getParametersCompletedEventArgs args);
    
    public partial class getParameterDetailsCompletedEventArgs : System.ComponentModel.AsyncCompletedEventArgs {
        
        private object[] results;
        
        internal getParameterDetailsCompletedEventArgs(object[] results, System.Exception exception, bool cancelled, object userState) : 
                base(exception, cancelled, userState) {
            this.results = results;
        }
        
        public wsParameterDetails Result {
            get {
                this.RaiseExceptionIfNecessary();
                return ((wsParameterDetails)(this.results[0]));
            }
        }
    }
    
    public delegate void getParameterDetailsCompletedEventHandler(object sender, getParameterDetailsCompletedEventArgs args);
}
