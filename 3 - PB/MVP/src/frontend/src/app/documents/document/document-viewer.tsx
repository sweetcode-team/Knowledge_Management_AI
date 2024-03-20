// import React, { useEffect } from 'react';
// import mammoth from 'mammoth';



// const MyComponent = () => {
//     useEffect(() => {
//       let element = document.getElementById("document");
//       if (element) {
//           element.addEventListener("change", handleFileSelect, false);
//       }
      

//         function handleFileSelect(event: Event) {
//             readFileInputEventAsArrayBuffer(event, function(arrayBuffer: ArrayBuffer) {
//                 mammoth.convertToHtml({arrayBuffer: arrayBuffer})
//                     .then(displayResult)
//                     .catch((error: Error) => console.error(error));
//             });
//         }


//         function displayResult(result: mammoth.ConvertToHtmlResult) {
//           document.getElementById("output")!.innerHTML = result.value;

//           var messageHtml = result.messages.map(function(message: any) {
//             return '<li class="' + message.type + '">' + escapeHtml(message.message) + "</li>";
//           }).join("");

//           document.getElementById("messages")!.innerHTML = "<ul>" + messageHtml + "</ul>";
//         }

//         function readFileInputEventAsArrayBuffer(event: Event, callback: (arrayBuffer: ArrayBuffer) => void) {
//             var file = (event.target as HTMLInputElement).files![0];

//             var reader = new FileReader();

//             reader.onload = function(loadEvent: ProgressEvent<FileReader>) {
//                 var arrayBuffer = loadEvent.target!.result as ArrayBuffer;
//                 callback(arrayBuffer);
//             };

//             reader.readAsArrayBuffer(file);
//         }

//         function escapeHtml(value: string) {
//             return value
//                 .replace(/&/g, '&')
//                 .replace(/</g, '<')
//                 .replace(/>/g, '>');
//         }
//     }, []);

//     return (
//         <div>
//             <input type="file" id="document" />
//             <div id="output"></div>
//             <div id="messages"></div>
//         </div>
//     );
// };

// export default MyComponent;
