angular.module('myApp', ['ui.router'])
.config(['$stateProvider', '$urlRouterProvider', function ($stateProvider, $urlRouterProvider) {

    $stateProvider
        .state('tab', {
            url: "/tab",
            // abstract为true, 表示抽象模板永远不能被激活, 但是可以设置被激活的子节点, 可以使用抽象模板包装器包裹多个命名视图, 或者传递事件给子节点
            abstract: true,
            templateUrl: "tab.html"
        })
        .state('tab.news', {
            url: "/news",
            templateUrl: "news.html"
        })
        .state('tab.live', {
            url: "/live",
            templateUrl: "live.html"
        })
        .state('tab.talk', {
            url: "/talk",
            templateUrl: "talk.html"
        })
        .state('tab.mine', {
            url: "/mine",
            templateUrl: "mine.html"
        });
    $urlRouterProvider.otherwise('/tab/news');


}]);