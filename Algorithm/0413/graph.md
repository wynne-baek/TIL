# graph

: 사물들과 이들 사이의 연결 관계를 표현

### 00. graph 기본 개념

- 구성요소 : 정점(V), 간선(E)
- 선형 자료구조나 트리 자료구조로 표현이 어려운 N:N 관계를 가지는 원소 표현에 용이
- 유형
  - 무향 그래프
  - 유향 그래프
  - 가중치 그래프
  - 사이클 없는 방향 그래프
  - 완전 그래프 : 정점들에 대해 가능한 모든 간선들을 가진 그래프
  - 부분 그래프 : 원래 그래프에서 일부의 정점이나 간선을 제외한 그래프

- 경로
  - 단순 경로 : 한 정점을 최대한 1번만 지나는 경로
  - 사이클 : 시작한 정점에서 끝나는 경로

- 그래프 순회(탐색)
  - BFS
  - DFS

### 01. 서로소 집합

- 서로소/상호배타 집합 : 중복 포함된 원소가 없는 집합, 교집합 X
- 집합에 속한 하나의 특정 멤버를 통해 각 집합들을 구분, 대표자 라고 함

- 표현 방법
  1. 연결 리스트
     - 같은 집합의 원소들은 하나의 연결리스트로 관리
     - 맨 앞 원소를 집합의 대표 원소로
     - 각 원소는 집합의 대표원소를 가리키는 링크를 가짐
  2. 트리
     - 하나의 집합을 하나의 트리로 표현
     - 자식 노드가 부모 노드를 가리키며 루트 노드가 대표자

### 02. 최소 신장 트리(MST)

- 그래프에서 최소 비용 문제

  1. 모든 정점을 연결하는 간선들의 가중치의 합이 최소가 되는 트리
  2. 두 정점 사이의 최소 비용의 경로 찾기

- 신장 트리

  : V 개의 정점으로 이루어진 무방향 그래프에서 V 개의 정점과 V-1 개의 간선으로 이루어진 트리

- 최소 신장 트리(Minimum Spanning Tree)

  : 무방향 가중치 그래프에서 신장 트리를 구성하는 간선들의 가중치의 합이 최소인 신장 트리